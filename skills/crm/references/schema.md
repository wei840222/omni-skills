# The Minimum Record

Start here whatever the tool. Every field below is used by a filter, a report, or a follow-up rule; anything that is not has to earn its place.

| Entity | Fields that earn their place | Identity |
|---|---|---|
| Person | id · name · email · org · role · preferred channel · tier · source · owner · next step + date · suppression flag | email (lowercased) |
| Organization | id · name · domain · segment · size band · primary contact id | domain |
| Deal | id · org id · primary contact id · value + currency · stage · stage-entered date · close date + as-of · next step + date · source · won/lost reason | id |
| Interaction | date · contact id · deal id (optional) · type (call/meeting/email/note) · direction · one line of substance · next step | date + contact id |

Use `tags` for anything a filter might want when a schema change should not cost: industry, event met at, warm/cold, referral source. Rigid categories only where a report groups by them. Notes are one field, not three — "notes", "comments", and "background" in the same record is how context becomes unfindable.
