"""Check that the privacy page still contains every approved statement and date, word for word.
Usage: python3 _project/scripts/check_privacy.py privacy/index.html
When you add or intentionally change a policy, update the LIVE list below to match."""
import sys, re, html
raw = open(sys.argv[1], encoding="utf-8").read()
text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", raw)))
LIVE = [
"One page, every app. Every Command Line Studios app is listed here with exactly what it does and doesn't collect.",
"Launchpad: Planetary Simulator does not collect, store, transmit, or share any personal information.",
"The app does not require you to create an account, does not use analytics or advertising services, and does not connect to the internet or send any data off your device. Every calculation the app performs happens entirely on your device.",
"Because no personal data is collected, none is shared with third parties, and none is sold. If Command Line Studios ever changes this practice in a future version of the app, this policy will be updated accordingly and the change will be clearly noted.",
"If you have questions about this policy, contact us at support@cmdlinestudios.com.",
"reps_: Your Digital Logbook does not collect, transmit, or share any personal information.",
"The app does not require you to create an account, does not use analytics or advertising services, and does not connect to the internet or send any data off your device. Your workouts, plan, and settings are stored only on your iPhone.",
"Nothing leaves your iPhone unless you choose to send it. When you export a backup or spreadsheet, or share a chart image, you decide where it goes. When you save a chart to Photos, the app can only add that image and cannot see your photo library. The rest timer on your lock screen and the \"Rest done\" notification are created on your iPhone (and may also appear on your paired Apple Watch); they never pass through a server.",
"Like any app's data, your workout data is included in your iPhone's own backups (iCloud or your computer), which Apple handles under your Apple Account settings.",
"More apps, more policies",
"// a section will appear here for each new app as it launches",
"Last updated: October 2026", "Last updated: November 2026",
]
bad = [s[:70] for s in LIVE if s not in text]
print("all privacy text matches" if not bad else "MISSING OR CHANGED: %r" % bad)
sys.exit(1 if bad else 0)
