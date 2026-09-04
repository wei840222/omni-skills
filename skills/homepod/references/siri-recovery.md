# HomePod Siri recovery map

Use this map when Siri hears the request but does not complete the intended Home action.

| Symptom | Likely cause | First check |
|---|---|---|
| “Working on that” then timeout | Service or permission path | Validate account and home permissions |
| Action runs in the wrong room | Ambiguous naming | Normalize room and accessory names |
| Correct action is delayed | Hub or network contention | Check home-hub state and network congestion |
| Siri cannot find an accessory | Discovery mismatch | Confirm accessory visibility in the Home app |

## Recovery sequence

1. Reproduce with one concise command for one accessory.
2. Ensure room and accessory names are unique and easy to distinguish.
3. Test the same action manually in the Home app. Restore the accessory control path before tuning Siri when the manual action fails.
4. Verify that the requesting user has the relevant home-control rights and that no stale invitation state remains.
5. Confirm which HomePod received the request; reduce location ambiguity when several speakers hear it.

Repeat the exact command three times under normal household conditions and test a frequently used room before closing the incident. Record pass and fail counts in `<state_root>/automation-log.md` when notes are enabled.
