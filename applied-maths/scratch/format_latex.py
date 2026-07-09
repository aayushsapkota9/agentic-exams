import os
import re

qns_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/applied-maths/past-qns/md"
files = sorted([f for f in os.listdir(qns_dir) if f.endswith('.md')])

# List of regex replacements to apply to the source markdown files (not wrapped in $)
replacements = [
    # Format variables
    (r'\bfunction f\(z\)', r'function $f(z)$'),
    (r'\bfunction f\(n\)', r'function $f(n)$'),
    (r'\bfunction f\(x\)', r'function $f(x)$'),
    (r'\bfunction f\(t\)', r'function $f(t)$'),
    (r'\bvariables u and v\b', r'variables $u$ and $v$'),
    (r'\bfunctions u and v\b', r'functions $u$ and $v$'),
    (r'\bimaginary part v\b', r'imaginary part $v$'),
    (r'\breal part u\b', r'real part $u$'),
    (r'\blength L\b', r'length $L$'),
    (r'\blength l\b', r'length $l$'),
    (r'\bradius R\b', r'radius $R$'),
    (r'\bside a = b = 1\b', r'side $a = b = 1$'),
    (r'\bconstant c = 1\b', r'constant $c = 1$'),
    (r'\bcontour C\b', r'contour $C$'),
    (r'\bcircle C\b', r'circle $C$'),
    (r'\bellipse C\b', r'ellipse $C$'),
    (r'\bwhere C\b', r'where $C$'),
    (r'\bpoint \(x,\s*y\)\b', r'point $(x, y)$'),
    (r'\bpoints \(x,\s*y\)\b', r'points $(x, y)$'),
    (r'\bdomain D\b', r'domain $D$'),
    (r'\bz-plane\b', r'$z$-plane'),
    (r'\bw-plane\b', r'$w$-plane'),
    (r'\bregion ABCD\b', r'region $ABCD$'),
    
    # Format equations and functions
    (r'u = e\^x \\cos y', r'$u = e^x \cos y$'),
    (r'u = e\^x \(\\cos y\)', r'$u = e^x \cos y$'),
    (r'u = e\^x \(x \\cos y - y \\sin y\)', r'$u = e^x (x \cos y - y \sin y)$'),
    (r'u = x\^2 - y\^2', r'$u = x^2 - y^2$'),
    (r'v = x\^3 - 3xy\^2', r'$v = x^3 - 3xy^2$'),
    (r'v = 3x\^2y - y\^3', r'$v = 3x^2y - y^3$'),
    (r'u = y\^3 - 3x\^2y', r'$u = y^3 - 3x^2y$'),
    (r'u = \\sin x \\cosh y', r'$u = \sin x \cosh y$'),
    (r'u = \\cos x \\cosh y', r'$u = \cos x \cosh y$'),
    (r'u = 3xy \+ x\^2 - y - y\^2', r'$u = 3xy + x^2 - y - y^2$'),
    (r'f\(z\) = u \+ i v', r'$f(z) = u + i v$'),
    (r'f\(z\) = u \+ iv', r'$f(z) = u + i v$'),
    (r'f\(z\) = \\bar\{z\}', r'$f(z) = \bar{z}$'),
    (r'f\(z\) = \\tan z', r'$f(z) = \tan z$'),
    (r'f\(z\) = \\sin z', r'$f(z) = \sin z$'),
    (r'f\(z\) = \\cos z', r'$f(z) = \cos z$'),
    (r'f\(z\) = \\cosh z', r'$f(z) = \cosh z$'),
    (r'z \\bar\{z\}', r'$z \bar{z}$'),
    (r'f\(z\) = z \\bar\{z\}', r'$f(z) = z \bar{z}$'),
    (r'f\(z\) = \\frac\{7z-2\}\{\(z\+1\)\(z-3\)\}', r'$f(z) = \frac{7z-2}{(z+1)(z-3)}$'),
    (r'f\(z\) = \\frac\{1\}\{\(z-1\)\(z-2\)\}', r'$f(z) = \frac{1}{(z-1)(z-2)}$'),
    (r'f\(z\) = \\frac\{1\}\{\(z-2\)\(z-3\)\}', r'$f(z) = \frac{1}{(z-2)(z-3)}$'),
    
    # Boundary/Limits
    (r'x = 1,\s*x = 3,\s*y = 0,\s*y = 3', r'$x = 1, x = 3, y = 0, y = 3$'),
    (r'y = 1,\s*y = 2,\s*x = 1,\s*x = 2', r'$y = 1, y = 2, x = 1, x = 2$'),
    (r'0 < y < \\frac\{\\pi\}\{2\}', r'$0 < y < \frac{\pi}{2}$'),
    (r'w = z \+ \(2 \+ i\)', r'$w = z + (2 + i)$'),
    (r'w = 3z', r'$w = 3z$'),
    (r'z = 0,\s*-1,\s*i', r'$z = 0, -1, i$'),
    (r'z = 0,\s*-i,\s*i', r'$z = 0, -i, i$'),
    (r'w = i,\s*0,\s*\\infty', r'$w = i, 0, \infty$'),
    (r'z_1 = \\infty,\s*z_2 = 1,\s*z_3 = 0', r'$z_1 = \infty, z_2 = 1, z_3 = 0$'),
    (r'w_1 = 0,\s*w_2 = i,\s*w_3 = \\infty', r'$w_1 = 0, w_2 = i, w_3 = \infty$'),
    
    # Curves/Contours
    (r'C:\s*\|z\| = 1\.5', r'$C: |z| = 1.5$'),
    (r'C:\s*\|z\| = 2', r'$C: |z| = 2$'),
    (r'C:\s*\|z\| = 3', r'$C: |z| = 3$'),
    (r'C:\s*\|z\| = 5', r'$C: |z| = 5$'),
    (r'C:\s*\|z-1\| = 1', r'$C: |z-1| = 1$'),
    (r'C:\s*\|z-1\| = 3', r'$C: |z-1| = 3$'),
    (r'C:\s*\|z-i\| = 1', r'$C: |z-i| = 1$'),
    (r'C:\s*\|z-i\| = 2', r'$C: |z-i| = 2$'),
    (r'C:\s*\|z\| = \\frac\{3\}\{2\}', r'$C: |z| = \frac{3}{2}$'),
    (r'\|z\| = 1', r'$|z| = 1$'),
    (r'\|z\| = 2', r'$|z| = 2$'),
    (r'\|z\| = 3', r'$|z| = 3$'),
    (r'\|z\| = 5', r'$|z| = 5$'),
    
    # C-R conditions
    (r'u_x = v_y', r'$u_x = v_y$'),
    (r'u_y = -v_x', r'$u_y = -v_x$'),
    (r'u_y = u_x', r'$u_y = u_x$'),
    (r'u_x = 2 u_t \+ u', r'$u_x = 2 u_t + u$'),
    
    # Z-Transform
    (r'Z\(a\^n\)', r'$Z(a^n)$'),
    (r'Z\(e\^\{an\}\)', r'$Z(e^{an})$'),
    (r'Z\(n a\^n\)', r'$Z(n a^n)$'),
    (r'Z\(n\^2\)', r'$Z(n^2)$'),
    (r'Z\(n\^2 e\^\{-an\}\)', r'$Z(n^2 e^{-an})$'),
    (r'Z\(3n\^2 - 2n \+ 1\)', r'$Z(3n^2 - 2n + 1)$'),
    (r'Z\(a\^n \\cos bn\)', r'$Z(a^n \cos bn)$'),
    (r'Z\(a\^n \\sin bn\)', r'$Z(a^n \sin bn)$'),
    (r'Z\(\\sin\(n\\theta\)\)', r'$Z(\sin(n\theta))$'),
    (r'Z\(\\cos\(n\\theta\)\)', r'$Z(\cos(n\theta))$'),
    (r'Z\(\\sin \\omega t\)', r'$Z(\sin \omega t)$'),
    (r'Z\(\\cos \\omega t\)', r'$Z(\cos \omega t)$'),
    (r'Z\(e\^\{-at\}\)', r'$Z(e^{-at})$'),
    (r'e\^\{-at\}', r'$e^{-at}$'),
    (r'\bn a\^n\b', r'$n a^n$'),
    (r'\ba\^n\b', r'$a^n$'),
    (r'\b2\^n\b', r'$2^n$'),
    (r'\b4\^n\b', r'$4^n$'),
    (r'\be\^\{an\}\b', r'$e^{an}$'),
    (r'\(1 - e\^\{-an\}\)\^2', r'$(1 - e^{-an})^2$'),
    (r'y_0 = 0,\s*y_1 = 0', r'$y_0 = 0, y_1 = 0$'),
    (r'y_0 = 0,\s*y_1 = 1', r'$y_0 = 0, y_1 = 1$'),
    (r'y_0 = 2,\s*y_1 = 1', r'$y_0 = 2, y_1 = 1$'),
    (r'u_\{n\+2\} - 2\\cos\\alpha\s*u_\{n\+1\} \+ u_n = 0', r'$u_{n+2} - 2\cos\alpha \, u_{n+1} + u_n = 0$'),
    (r'y_\{n\+2\} - 7y_\{n\+1\} \+ 12y_n = 2\^n', r'$y_{n+2} - 7y_{n+1} + 12y_n = 2^n$'),
    (r'y_\{n\+2\} - 4y_\{n\+1\} \+ 4y_n = 2\^n', r'$y_{n+2} - 4y_{n+1} + 4y_n = 2^n$'),
    (r'y_\{n\+2\} - 3y_\{n\+1\} \+ 2y_n = 4\^n', r'$y_{n+2} - 3y_{n+1} + 2y_n = 4^n$'),
    (r'y_\{n\+2\} - 2y_\{n\+1\} \+ y_n = 2\^n', r'$y_{n+2} - 2y_{n+1} + y_n = 2^n$'),
    (r'y_\{n\+2\} \+ 6y_\{n\+1\} \+ 9y_n = 2\^n', r'$y_{n+2} + 6y_{n+1} + 9y_n = 2^n$'),
    (r'y_\{n\+2\} \+ 3y_\{n\+1\} \+ 2y_n = 0', r'$y_{n+2} + 3y_{n+1} + 2y_n = 0$'),
    (r'Z\^\{-1\}\\left\[\s*\\frac\{z\^2\+z\}\{z\^2-2z\+2\}\s*\\right\]', r'$Z^{-1}\left[ \frac{z^2+z}{z^2-2z+2} \right]$'),
    (r'Z\^\{-1\}\\left\[\s*\\frac\{z\^2\+2z\}\{\(z-1\)\^2\}\s*\\right\]', r'$Z^{-1}\left[ \frac{z^2+2z}{(z-1)^2} \right]$'),
    (r'Z\^\{-1\}\\left\[\s*\\frac\{3z\^2 - 18z \+ 26\}\{\(z-2\)\(z-3\)\^2\}\s*\\right\]', r'$Z^{-1}\left[ \frac{3z^2 - 18z + 26}{(z-2)(z-3)^2} \right]$'),
    (r'F\(z\) = \\frac\{z\^2\+z\}\{z\^2-2z\+2\}', r'$F(z) = \frac{z^2+z}{z^2-2z+2}$'),
    (r'F\(z\) = \\frac\{3z\^2 \+ 2z \+ 1\}\{z\^2 - 3z \+ 2\}', r'$F(z) = \frac{3z^2 + 2z + 1}{z^2 - 3z + 2}$'),
    
    # PDEs
    (r'u_\{xx\} \+ 9u = 0', r'$u_{xx} + 9u = 0$'),
    (r'u_\{xx\} - u_\{yy\} = 0', r'$u_{xx} - u_{yy} = 0$'),
    (r'u_\{xx\} \+ u_\{yy\} = 0', r'$u_{xx} + u_{yy} = 0$'),
    (r'u\(x,\s*t\)', r'$u(x, t)$'),
    (r'u\(x,\s*y,\s*t\)', r'$u(x, y, t)$'),
    (r'u\(x,\s*0\) = f\(x\)', r'$u(x, 0) = f(x)$'),
    (r'u\(x,\s*0\) = 3 \\sin\\left\(\\frac\{\\pi x\}\{L\}\\right\)', r'$u(x, 0) = 3 \sin\left(\frac{\pi x}{L}\right)$'),
    (r'u\(0,\s*t\) = 0 = u\(L,\s*t\)', r'$u(0, t) = 0 = u(L, t)$'),
    (r'u\(0,\s*t\) = 0', r'$u(0, t) = 0$'),
    (r'u\(L,\s*t\) = 0', r'$u(L, t) = 0$'),
    (r'u\(100,\s*t\) = 0', r'$u(100, t) = 0$'),
    (r'u\(0,\s*y\) = u\(l,\s*y\) = u\(x,\s*0\) = 0', r'$u(0, y) = u(l, y) = u(x, 0) = 0$'),
    (r'u\(x,\s*a\) = \\sin\\left\(\\frac\{\\pi x\}\{l\}\\right\)', r'$u(x, a) = \sin\left(\frac{\pi x}{l}\right)$'),
    (r'f\(x\) = \\sin\^3\\(0\.01\\pi x\\)', r'$f(x) = \sin^3(0.01\pi x)$'),
    (r'f\(x\) = \\sin\\(0\.01\\pi x\\)', r'$f(x) = \sin(0.01\pi x)$'),
    (r'f\(x\) = \\sin\^3\\(\\frac\{\\pi x\}\{L\}\\)', r'$f(x) = \sin^3\left(\frac{\pi x}{L}\right)$'),
    (r'f\(x\) = x\(L-x\)', r'$f(x) = x(L-x)$'),
    (r'g\(x\) = x', r'$g(x) = x$'),
    (r'f\(x\) = x', r'$f(x) = x$'),
    (r'v\(x\) = kx\(l - x\)', r'$v(x) = kx(l - x)$'),
    (r'c\^2 = 0\.175', r'$c^2 = 0.175$'),
    (r'c\^2 = 1\.158', r'$c^2 = 1.158$'),
    (r'c\^2 = 1', r'$c^2 = 1$'),
    (r'c = 1', r'$c = 1$'),
    (r'a = b = 1', r'$a = b = 1$'),
    (r'L = \\pi', r'$L = \pi$'),
    (r'0 < x < L', r'$0 < x < L$'),
    (r'0 < x < 10', r'$0 < x < 10$'),
    (r'10 < x < 20', r'$10 < x < 20$'),
    (r'0 \\le x < 50', r'$0 \le x < 50$'),
    (r'50 \\le x < 100', r'$50 \le x < 100$'),
    (r'0 < x < 8', r'$0 < x < 8$'),
    (r'y = 0', r'$y = 0$'),
    (r'x = 0', r'$x = 0$'),
    (r'x = 8', r'$x = 8$'),
    (r'u\(x,\s*0\) = 100 \\sin\\left\(\\frac\{\\pi x\}\{8\}\\right\)', r'$u(x, 0) = 100 \sin\left(\frac{\pi x}{8}\right)$'),
    
    # Fourier Transform
    (r'f\(x\) = e\^\{-mx\}', r'$f(x) = e^{-mx}$'),
    (r'e\^\{-mx\}', r'$e^{-mx}$'),
    (r'm > 0', r'$m > 0$'),
    (r'a > 0', r'$a > 0$'),
    (r'x > 0', r'$x > 0$'),
    (r'f\(x\) = e\^\{-px\}', r'$f(x) = e^{-px}$'),
    (r'f\(x\) = e\^\{-ax\}', r'$f(x) = e^{-ax}$'),
    (r'f\(x\) = e\^\{-x\}', r'$f(x) = e^{-x}$'),
    (r'f\(x\) = e\^\{-\|x\|\}', r'$f(x) = e^{-|x|}$'),
    (r'e\^\{-\|x\|\}', r'$e^{-|x|}$'),
    (r'f\(x\) = x', r'$f(x) = x$'),
    (r'0 < x < 1', r'$0 < x < 1$'),
    (r'x > 1', r'$x > 1$'),
    (r'x < 0', r'$x < 0$')
]

def apply_replacements(text):
    # Sort replacements by length of pattern in reverse order so we match longest patterns first
    for pattern, replacement in sorted(replacements, key=lambda x: len(x[0]), reverse=True):
        regex = re.compile(pattern)
        text = regex.sub(lambda m, r=replacement: r, text)
    return text

def process_line(line, in_display_math):
    if in_display_math:
        return line
        
    # 1. Extract existing math blocks ($...$ and $$...$$) to avoid double-processing
    placeholders = {}
    
    def repl_existing(match):
        placeholder = f"___MATH_BLOCK_{len(placeholders)}___"
        placeholders[placeholder] = match.group(0)
        return placeholder

    # Replace display math $$...$$ first, then inline $...$
    processed_line = re.sub(r'\$\$.*?\$\$', repl_existing, line)
    processed_line = re.sub(r'\$.*?\$', repl_existing, processed_line)
    
    # 2. Apply replacements on the text that has no math blocks
    processed_line = apply_replacements(processed_line)
    
    # 3. Restore math blocks
    for _ in range(5):
        changed = False
        for placeholder, val in placeholders.items():
            if placeholder in processed_line:
                processed_line = processed_line.replace(placeholder, val)
                changed = True
        if not changed:
            break
            
    return processed_line

def process_file_content(content):
    lines = content.split('\n')
    new_lines = []
    in_display_math = False
    
    for line in lines:
        contains_display_marker = '$$' in line
        
        if contains_display_marker:
            if in_display_math:
                # Ends display math
                in_display_math = False
                new_lines.append(line)
            else:
                # Starts display math
                # If there are two or more $$ (e.g. $$x = 1$$), it starts and ends on same line
                if line.count('$$') >= 2:
                    new_lines.append(line)
                else:
                    in_display_math = True
                    new_lines.append(line)
            continue
            
        # process line passing current in_display_math state
        new_lines.append(process_line(line, in_display_math))
        
    return '\n'.join(new_lines)

for filename in files:
    filepath = os.path.join(qns_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    content = process_file_content(content)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Formatted LaTeX in {filename}")
