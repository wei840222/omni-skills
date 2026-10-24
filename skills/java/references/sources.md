# Official Sources & Language Specifications

This document records the authoritative language specifications, virtual machine standards, and OpenJDK project documentation for Java and the JVM.

## Official Standards & Specifications

- **Oracle Java SE 21 Documentation**: [https://docs.oracle.com/en/java/javase/21/](https://docs.oracle.com/en/java/javase/21/)
  - Standard library APIs, garbage collection options (G1, ZGC, Parallel), compiler tools, and security architecture.
- **Java Language Specification (Java SE 21 Edition)**: [https://docs.oracle.com/javase/specs/jls/se21/html/index.html](https://docs.oracle.com/javase/specs/jls/se21/html/index.html)
  - Formal language grammar, type system, record patterns, sealed classes, and Java Memory Model (JMM).
- **The Java Virtual Machine Specification (Java SE 21 Edition)**: [https://docs.oracle.com/javase/specs/jvms/se21/html/index.html](https://docs.oracle.com/javase/specs/jvms/se21/html/index.html)
  - Bytecode verification, class loading hierarchies, memory allocation, and frame execution semantics.
- **OpenJDK Project Loom (Virtual Threads - JEP 444)**: [https://openjdk.org/jeps/444](https://openjdk.org/jeps/444)
  - Lightweight user-mode threads, carrier thread pinning (`synchronized` caveats), and high-throughput concurrent I/O.
