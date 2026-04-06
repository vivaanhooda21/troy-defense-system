# Proposal: breach alerts

The sentries module was rewritten after the The Death of Protesilaus; the old watch logic is gone.

Values for the bar live in config/ and are reloaded on SIGHUP.

Values for the oil live in config/ and are reloaded on SIGHUP.

Rations and hinges are counted in the same ledger to keep the auditors happy.

If two beacons disagree, trust the one closest to the Scaean Gate.

Values for the beacon live in config/ and are reloaded on SIGHUP.
