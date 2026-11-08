"""Owner's real photos from Google Drive (Photoshoots/*), referenced by file ID.
Rendered via Drive's public image endpoint — requires the folders be
"Anyone with link" (owner toggles this). Graceful fallback hides any that
aren't public yet."""

# Branded boxes, crates & packing tape (Photoshoots/Boxes)
BOX_IDS = [
    "1ZkDlhXgHzX1vh8WpFoIOq05phJKAVXQt", "16qJ6QeySxsyanEzbZKrHmy794V-JiKCe",
    "19c02apim0dZwlrs-Q2kIEr1_b8nOP8dE", "1z5RBgMFT7uBClaJxFVoVxV98cNpAZbVp",
    "11WekY74iZUQdXOAAQt9Eji2fFqTFmm5f", "18O5jlKkyXbSNP7eY17WJV6sP3RnT1VV2",
    "1c1zPLoVlx6qVnLFPRPTFVBH---JmAqRm", "12otzk-k5U1YX8mRmdZTfkXUavDv5UYM1",
]

# Professional team / staff in branded polos (Photoshoots/Shoot-November-2025)
STAFF_IDS = [
    "1tnUD9a75AzP5_iAx28QbynpfBUD6h3hV",  # 3969 group
    "14caFF6-USKCwLPmwkKE85FfqCmosFIFh",  # 3963 group
    "1RZ22a9h92MFuepHyeUb9DogUYlUl2GWR",  # 3971 group
    "1jmc5aojPbRufl0NK4s_VVffFN1xGifxX",  # 3973 group
    "1RTao6PpPnFZI3ZXOEF8tC_IwLzHnn49m",  # 3976 group
    "1wJuwONI4XaGhNYWaMuilf3CH-1OxnpbM",  # 3978 group
]
TEAM_TRUCK = "1jCJEUR6kjRxBfkvvWi__RmJ6TJlbk7BZ"   # 3981 team in front of branded truck
STAFF_SOLO = "1S3wh3cxTkUdzrsJL5Vy7aDtHiH6jfkn_"   # 3960 single staff with materials

# In-home lifestyle shots: people with branded boxes in customers' homes (Raw Gallery-12-10-2024)
LIFESTYLE_IDS = [
    "1I6qaRQ75jR6Gp2yLP9fcQsu1kW3-i14r", "1OrRxjZ89cLdsX7yUPHkCl24cLg0kAPrD",
    "1j1GUlVQ1KyHiv0ZA-bUTyf1eNrHDpTZn", "1BO2LYsxS1ht9SBspxcPRJvytK-QMBYkL",
    "1m-HSwhnuGMFtbRKm0zxHabxQ_rGz1jDg", "1w1cTKX9kYJXDzI3O0g5iAIOvCB59TUuE",
    "1oGPS_Bcag1udvBJgL9639I3Wmdul7V5E", "1Y5W6DZnQCDldRni5kZzMVkXs-iWazPe1",
]


def img(fid, w=900):
    return f"https://lh3.googleusercontent.com/d/{fid}=w{w}"


def gallery(ids, alt="Universal Relocations", title="", sub="", eyebrow="Gallery"):
    import expand as X
    items = "".join(
        f'<figure class="dg-item"><img loading="lazy" src="{img(i)}" alt="{alt}" '
        f'onerror="this.closest(&quot;.dg-item&quot;).style.display=&quot;none&quot;"></figure>'
        for i in ids)
    head = X.sec_head(title, sub, eyebrow) if title else ""
    return X.isec(f'<div class="dgrid">{items}</div>', alt=True, head=head)
