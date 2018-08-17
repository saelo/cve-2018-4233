# CVE-2018-4233

Exploit for CVE-2018-4233, a bug in the JIT compiler of WebKit. Tested on Safari 11.0.3 on macOS 10.13.3.

For more details see https://saelo.github.io/presentations/blackhat_us_18_attacking_client_side_jit_compilers.pdf

The exploit gains arbitrary memory read/write by constructing the addrof and fakeobj primitives and subsequently faking a typed array as described in http://www.phrack.org/papers/attacking_javascript_engines.html. Afterwards it locates the JIT page and writes the stage1 shellcode there. That in turn writes a .dylib (contained in stage2.js) to disk and loads it into the renderer process to perform a sandbox escape. Stage 2 uses a separate vulnerability to break out of the Safari sandbox and will be published at a later point.
