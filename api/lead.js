// Vercel Serverless Function — receives a lead from the Move Assistant.
// Forwards to a configurable destination (CRM webhook and/or email).
//
// Configure in Vercel → Project → Settings → Environment Variables:
//   LEAD_WEBHOOK_URL   e.g. your MacroFunnel / CRM inbound-lead webhook (POST JSON)
//   LEAD_NOTIFY_EMAIL  (optional) address to notify, used with RESEND_API_KEY
//   RESEND_API_KEY     (optional) Resend API key to send the email notification
//
// With none set, the lead is still accepted (logged in Vercel function logs) so
// the visitor always sees success — wire a destination to actually receive them.

export default async function handler(req, res) {
  // Basic CORS (same-origin in practice, but harmless)
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "Method not allowed" });

  let lead = {};
  try {
    lead = typeof req.body === "object" && req.body ? req.body : JSON.parse(req.body || "{}");
  } catch (_) {
    return res.status(400).json({ ok: false, error: "Invalid JSON" });
  }

  // Minimal validation: need at least one way to contact them
  if (!lead.email && !lead.phone) {
    return res.status(400).json({ ok: false, error: "A contact email or phone is required" });
  }

  const payload = {
    source: "universal-relocations-move-assistant",
    receivedAt: new Date().toISOString(),
    name: lead.name || "",
    email: lead.email || "",
    phone: lead.phone || "",
    moveType: lead.moveType || "",
    route: lead.route || "",
    from: lead.from || "",
    to: lead.to || "",
    size: lead.size || "",
    moveDate: lead.date || "",
    estimate: lead.estimate || ""
  };

  // Always log — visible in Vercel → Deployments → Functions logs
  console.log("NEW LEAD:", JSON.stringify(payload));

  const tasks = [];

  // 1) Forward to CRM / webhook if configured
  if (process.env.LEAD_WEBHOOK_URL) {
    tasks.push(
      fetch(process.env.LEAD_WEBHOOK_URL, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload)
      }).catch((e) => console.error("Webhook forward failed:", e.message))
    );
  }

  // 2) Optional email notification via Resend
  if (process.env.RESEND_API_KEY && process.env.LEAD_NOTIFY_EMAIL) {
    const lines = Object.entries(payload)
      .map(([k, v]) => `<b>${k}:</b> ${String(v || "—")}`)
      .join("<br>");
    tasks.push(
      fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          "content-type": "application/json",
          Authorization: `Bearer ${process.env.RESEND_API_KEY}`
        },
        body: JSON.stringify({
          from: "Move Assistant <onboarding@resend.dev>",
          to: [process.env.LEAD_NOTIFY_EMAIL],
          subject: `New move lead: ${payload.name || payload.email} (${payload.from} → ${payload.to})`,
          html: `<h2>New lead from the Move Assistant</h2>${lines}`
        })
      }).catch((e) => console.error("Email notify failed:", e.message))
    );
  }

  await Promise.allSettled(tasks);
  return res.status(200).json({ ok: true });
}
