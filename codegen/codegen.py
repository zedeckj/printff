def gen_macro():
    chars = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
    macros = []
    MAX_C = 26 * 2 + 1
    for argc in range(MAX_C):
        args = [chars[i] for i in range(argc)]
        body_args = ",".join(["fmt"] + [f"_ANNOTATE({a})" for a in args])
        args = ",".join(["fmt"] + args)
        body = f"printff_func({body_args})"
        macros.append(f"#define _PRINTFF{argc + 1}({args}) {body}")
    macros = "\n\n".join(macros)
    macro_names = list(reversed([f" _PRINTFF{i} " for i in range(1, MAX_C)]))
    ovr_args = ",".join([f"_{i}" for i in range(1,MAX_C)] + ["NAME", "..."])
    macros += f"\n\n#define _OVERRIDE_PRINTFF({ovr_args}) NAME"
    macros += f"\n\n#define printff(...) _OVERRIDE_PRINTFF(__VA_ARGS__, {",".join(macro_names)})(__VA_ARGS__)\n\n#endif"
    return macros 
with open("prelude.txt", "r") as f:
    prelude = f.read() + "\n"

with open("post.txt", "r") as f:
    post = "\n" + f.read() + "\n"

with open("../printff.h", "w") as f:
    f.write(prelude + gen_macro() + post)
    print("code gen complete")
