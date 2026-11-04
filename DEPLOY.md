# Universal Relocations — deploy to Vercel

Static site, no build step. From inside this folder:

    npm i -g vercel     # once
    vercel login        # once, in your browser
    vercel --prod       # deploys to production

Vercel auto-detects it as a static site; vercel.json is already set up.
Framework preset: "Other". No install/build command needed.
