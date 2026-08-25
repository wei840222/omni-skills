# Office Open XML (OOXML) Format

Office Open XML (OOXML) is a zipped, XML-based file format developed by Microsoft for representing spreadsheets, charts, presentations, and word processing documents. It is the underlying structure of modern `.docx` files.

## Technical Specifications
- **Standardization**: Initially standardized by Ecma International as ECMA-376, and later by ISO/IEC as ISO/IEC 29500.
- **Support**: Microsoft Office 2010 provides read support for ECMA-376 and ISO/IEC 29500 Transitional. Office 2013 and later fully support ISO/IEC 29500 Strict (though Transitional is still heavily used for backwards compatibility).
- **Structure**: A `.docx` file is a ZIP archive containing multiple XML parts and relationships. The key document parts include `word/document.xml` (main content), `styles.xml` (style definitions), `numbering.xml` (list styles), and various header/footer parts.
- **Complexity**: OOXML is highly complex compared to plain text or standard HTML. Features like tracked changes, numbering lists, section properties, and styles interact intricately. Direct formatting can override named styles, but relying on styles is best for document stability.
- **References**: Wikipedia (Office Open XML, ECMA-376, ISO/IEC 29500).
