# Trigger Evaluation

This review checks the `photography` description with realistic requests. The prompts are advisory and do not create user state.

| ID | Prompt | Expected route | Observed result |
|---|---|---|---|
| P1 | "My indoor basketball photos are blurry. What camera settings should I change?" | Activate `photography` | Activate: camera settings and an image problem are in scope. |
| P2 | "Can you help me organize backups for my RAW wedding photos?" | Activate `photography` | Activate: photography backup workflow is in scope. |
| N1 | "Can you retouch this scanned family photo in Photoshop for me?" | Route to an image-editing skill | Route outside `photography`: this requests hands-on image editing rather than advisory photography guidance. |
| N2 | "Write a React app that displays images from my camera." | Route to a software skill | Route outside `photography`: this is software implementation. |
