# Official Sources (last-checked 2026-09-18)

Use these primary sources when verifying document-scan library behavior, CDN URLs, or OpenCV.js loading notes. Prefer the live page over memorized snippets.

## Core libraries
- jscanify repository — browser/Node document edge detection and perspective correction via https://github.com/ColonelParrot/jscanify
- jscanify npm package — install metadata and published package entry via https://www.npmjs.com/package/jscanify
- OpenCV.js docs — browser OpenCV build loading and API orientation via https://docs.opencv.org/

## CDN and delivery anchors
- jsDelivr GitHub CDN — load `jscanify` without a global install via https://cdn.jsdelivr.net/gh/ColonelParrot/jscanify@master/src/jscanify.min.js
- OpenCV.js 4.7.0 browser build — common companion script used with jscanify demos via https://docs.opencv.org/4.7.0/opencv.js

## Operational note
CDN pin paths and OpenCV.js builds can move. Re-check the linked pages before shipping a permanent production dependency; for one-off local previews, the lowest-friction CDN path is acceptable when the user only needs a single scan.
