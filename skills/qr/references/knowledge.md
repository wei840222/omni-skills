# QR domain knowledge

## Design defaults

- The QR Code standard defines four error-correction levels: L (about 7%), M (about 15%), Q (about 25%), and H (about 30%) restoration capability. Higher levels reduce available payload capacity.
- Reserve a quiet zone of at least four modules around the symbol. Keep modules solid and use a light background with dark modules so finder patterns remain distinct.
- A logo, decorative modules, low contrast, glare, poor print quality, and excessive payload density can reduce real-world scan reliability. Test the actual rendered code instead of assuming a styling choice is safe.

## Size and scanning context

- A practical starting point is a symbol width of roughly one-tenth of the expected scan distance. Treat it as a sizing heuristic, then validate with representative devices and lighting.
- Shorter URLs and compact payloads produce fewer modules, leaving larger modules at the same printed size and generally improving scan tolerance.

## Sources

- QR Code error-correction levels and symbol characteristics: https://www.qrcode.com/en/about/error_correction.html
- QR Code quiet-zone requirements: https://www.qrcode.com/en/howto/cell.html
- ISO/IEC 18004 QR Code specification catalogue entry: https://www.iso.org/standard/83389.html
