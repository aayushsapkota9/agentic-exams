# Chapter 2: Z-Transform and its Applications — Past Questions
### Quick Navigation
[Z-Transform Definition & Properties](#z-transform-definition--properties) | [Inverse Z-Transform](#inverse-z-transform) | [Difference Equations](#difference-equations) | [Short Questions](#short-questions)

---

> [!NOTE]
> 🏛️ = **Pokhara University Board Exam** &nbsp;|&nbsp; All other entries are internal assessments, pre-board, or affiliate college exams.

---

## Z-Transform Definition & Properties

### Finding Z-Transforms / Shifting Theorems

##### 🏛️ 2025 Fall — Pokhara University (Board)
a) Define the Z-transform of a function $f(n)$. Find the Z-transform of $e^{i n \theta / 2}$ and hence find $Z\left[\cos\left(\frac{n\theta}{2}\right)\right]$ and $Z\left[\sin\left(\frac{n\theta}{2}\right)\right]$. **[8]**

b) Solve the difference equation:
$$u_{n+2} - 2\cos\alpha \, u_{n+1} + u_n = 0$$
by using Z-transform. **[7]**

```markdown
a) Define the Z-transform of a function $f(n)$. Find the Z-transform of $e^{i n \theta / 2}$ and hence find $Z[\cos(n\theta/2)]$ and $Z[\sin(n\theta/2)]$. **[8]**
b) Solve the difference equation $u_{n+2} - 2\cos\alpha\, u_{n+1} + u_n = 0$ using Z-transform. **[7]**
```

---

##### 🏛️ 2025 Spring — Pokhara University (Board)
b) Define Z-transform of a function. Prove that $Z[a^n f(t)] = F\left(\frac{z}{a}\right)$, where $Z[f(t)] = F(z)$. Using it, find $Z(a^n e^{bt})$ and hence deduce the values of $Z(a^n \cos bt)$ and $Z(a^n \sin bt)$. **[8]**

```markdown
b) Define Z-transform. Prove $Z[a^n f(t)] = F(z/a)$, where $Z[f(t)] = F(z)$. Using it, find $Z(a^n e^{bt})$ and hence deduce $Z(a^n \cos bt)$ and $Z(a^n \sin bt)$. **[8]**
```

---

##### 🏛️ 2024 Spring — Pokhara University (Board)
a) State and prove the first shifting theorem on Z-transform. Find the Z-transform of $e^{-at}$ and then find $Z\left(\cos \frac{\theta}{2}\right)$ and $Z\left(\sin \frac{\theta}{2}\right)$. **[8]**

b) Solve the difference equation:
$$y_{n+2} - 7y_{n+1} + 12y_n = 2^n$$
with $y_0 = 0, y_1 = 0$ by using Z-transform. **[7]**

c) Show that $Z[n f(t)] = -z \frac{d}{dz} [F(z)]$, where $F(z) = Z[f(t)]$. **[7]**

```markdown
a) State and prove first shifting theorem on Z-transform. Find Z-transform of $e^{-at}$ and then find $Z(\cos\theta/2)$ and $Z(\sin\theta/2)$. **[8]**
b) Solve $y_{n+2} - 7y_{n+1} + 12y_n = 2^n$, $y_0 = y_1 = 0$, using Z-transform. **[7]**
c) Show that $Z[nf(t)] = -z\frac{d}{dz}[F(z)]$. **[7]**
```

---

##### 🏛️ 2024 Fall — Pokhara University (Board)
a) State and prove first shifting theorem on Z-transform. Find Z-transform of $e^{in\pi/2}$ and then find $Z(\cos n\pi/2)$ and $Z(\sin n\pi/2)$. **[7]**

b) Solve the difference equation:
$$y_{n+2} - 7y_{n+1} + 12y_n = 2n$$
with $y_0 = 0$, $y_1 = 0$ by using Z-transform. **[8]**

c) Show that $Z[nf(t)] = -z \frac{d}{dz}[F(z)]$, where $F(z) = Z[f(t)]$. Find $Z^{-1}\left[\frac{z}{(z+1)^2(z-1)}\right]$. **[7]**

```markdown
a) State and prove first shifting theorem on Z-transform. Find Z-transform of $e^{in\pi/2}$, $Z(\cos n\pi/2)$, $Z(\sin n\pi/2)$. **[7]**
b) Solve $y_{n+2} - 7y_{n+1} + 12y_n = 2n$, $y_0 = y_1 = 0$, using Z-transform. **[8]**
c) Show $Z[nf(t)] = -z\frac{d}{dz}[F(z)]$. Find $Z^{-1}[z/(z+1)^2(z-1)]$. **[7]**
```

---

##### 2024 Spring — NAST (Pre-University)
a) Define Z-transform of a function $f(n)$. Find the Z-transform of $e^{i n \pi / 2}$ and hence find $Z[\cos(n\pi/2)]$ and $Z[\sin(n\pi/2)]$. **[8]**

```markdown
a) Define Z-transform. Find the Z-transform of $e^{in\pi/2}$ and hence find $Z[\cos(n\pi/2)]$ and $Z[\sin(n\pi/2)]$. **[8]**
```

---

##### 2024 Spring — Lumbini Engineering, Management & Science College / LEMSC (Final Internal)
a) State and prove the Second Shifting Theorem of Z-transform. Obtain the Z-transform of $(1 - e^{-an})^2$. **[8]**

```markdown
a) State and prove the Second Shifting Theorem of Z-transform. Obtain the Z-transform of $(1-e^{-an})^2$. **[8]**
```

---

##### 2024 Spring — Nepal Engineering College / NEC (Assessment)
a) State and prove the first shifting theorem of Z-transform. Obtain the inverse Z-transform:
$$Z^{-1}\left[ \frac{3z^2 - 18z + 26}{(z-2)(z-3)^2} \right]$$
**[8]**

```markdown
a) State and prove the first shifting theorem of Z-transform. Obtain $Z^{-1}\left[\frac{3z^2-18z+26}{(z-2)(z-3)^2}\right]$. **[8]**
```

---

##### 2024 Spring — Pokhara Engineering College / PEC (Final Internal)
b) Find the Z-transform of $e^{-at}$ and then deduce the values of $Z(\cos \omega t)$ and $Z(\sin \omega t)$. **[8]**

c) State and prove the first shifting theorem of Z-transform. Use it to evaluate $Z(n a^n)$ and $Z(e^{-an})$. **[7]**

```markdown
b) Find the Z-transform of $e^{-at}$ and deduce $Z(\cos\omega t)$ and $Z(\sin\omega t)$. **[8]**
c) State and prove first shifting theorem of Z-transform. Evaluate $Z(na^n)$ and $Z(e^{-an})$. **[7]**
```

---

##### 2024 Spring — Universal Engineering & Science College / UESC (Pre-Board)
a) Define Z-transform. State and prove the Second Shifting Theorem (time-delay theorem) of Z-transform. Evaluate $Z(n^2 e^{-an})$. **[7]**

**OR**

Find the inverse Z-transform:
$$Z^{-1}\left[ \frac{z^2+z}{z^2-2z+2} \right]$$
**[7]**

```markdown
a) Define Z-transform. State and prove the Second Shifting Theorem of Z-transform. Evaluate $Z(n^2 e^{-an})$. **[7]**
```

---

##### 2024 Spring — Madan Bhandari College of Engineering / MBCE (Final Internal)
a) State and prove the first shifting theorem of Z-transform. Evaluate the Z-transform of $a^n \cos(bn)$ and $a^n \sin(bn)$. **[8]**

```markdown
a) State and prove the first shifting theorem of Z-transform. Evaluate the Z-transform of $a^n\cos(bn)$ and $a^n\sin(bn)$. **[8]**
```

---

##### 2024 Spring — NCIT (Assessment)
a) Find the Z-transform of $e^{-at}$ and then find $Z(\cos \omega t)$ and $Z(\sin \omega t)$. **[7]**

```markdown
a) Find the Z-transform of $e^{-at}$ and then find $Z(\cos\omega t)$ and $Z(\sin\omega t)$. **[7]**
```

---

##### 2024 Spring — Everest Engineering College (Pre-Board)
b) Define Z-transform. State and prove the First Shifting Theorem of Z-transform. Also, prove that:
$$Z(n^2) = \frac{z(z+1)}{(z-1)^3}$$
and then use it to find $Z(n^2 e^{-an})$. **[7]**

```markdown
b) Define Z-transform. State and prove the First Shifting Theorem. Prove $Z(n^2) = z(z+1)/(z-1)^3$ and find $Z(n^2 e^{-an})$. **[7]**
```

---

##### 2024 Fall — United Technical College / UTC (Assessment)
a) If $f(n) = 0$ for $n < 0$ such that $Z(f(n)) = F(z)$, prove the time-delay theorem (second shifting theorem):
$$Z(f(n-k)) = z^{-k} F(z)$$
where $n > 0$, $k > 0$. **[8]**

```markdown
a) Prove the time-delay theorem (second shifting theorem): $Z(f(n-k)) = z^{-k}F(z)$. **[8]**
```

---

##### 31 — Pokhara University (Affiliate)
a) Define Z-transform. State and prove the first shifting theorem of Z-transform. Find $Z(a^n)$ and then use it to find $Z(a^n \cos bn)$ and $Z(a^n \sin bn)$. **[8]**

c) Show that $Z[n f(t)] = -z \frac{d}{dz}[F(z)]$, where $F(z) = Z[f(t)]$. **[7]**

```markdown
a) Define Z-transform. State and prove first shifting theorem. Find $Z(a^n)$, then $Z(a^n\cos bn)$ and $Z(a^n\sin bn)$. **[8]**
c) Show that $Z[nf(t)] = -z\frac{d}{dz}[F(z)]$. **[7]**
```

---

## Inverse Z-Transform

##### 🏛️ 2025 Spring — Pokhara University (Board)
a) Find:
1. $Z^{-1}\left[\frac{z}{z^2 - 5z + 6}\right]$ **[3]**
2. $Z^{-1}\left[\frac{z}{(z + 2)(z - 1)^2}\right]$ **[4]**

```markdown
a) Find: i. $Z^{-1}\left[\frac{z}{z^2-5z+6}\right]$ [3] ii. $Z^{-1}\left[\frac{z}{(z+2)(z-1)^2}\right]$ [4]
```

---

##### 2024 Spring — Nepal Engineering College / NEC (Assessment)
a) Obtain the inverse Z-transform:
$$Z^{-1}\left[ \frac{3z^2 - 18z + 26}{(z-2)(z-3)^2} \right]$$
**[as part of Q3a]**

```markdown
a) Obtain $Z^{-1}\left[\frac{3z^2-18z+26}{(z-2)(z-3)^2}\right]$.
```

---

##### 2024 Spring — Pokhara Engineering College / PEC (Final Internal)
a) Find the inverse Z-transform of:
$$F(z) = \frac{3z^2 + 2z + 1}{z^2 - 3z + 2}$$
**[8]**

```markdown
a) Find the inverse Z-transform of $F(z) = \frac{3z^2+2z+1}{z^2-3z+2}$. **[8]**
```

---

##### 2024 Fall — United Technical College / UTC (Assessment)
b) Find the Z-transform of $\sin \omega t$. **[3.5]**

c) Find $Z^{-1}\left[ \frac{z^2+2z}{(z-1)^2} \right]$. **[3.5]**

```markdown
b) Find the Z-transform of $\sin\omega t$. **[3.5]**
c) Find $Z^{-1}\left[\frac{z^2+2z}{(z-1)^2}\right]$. **[3.5]**
```

---

## Difference Equations

##### 🏛️ 2025 Fall — Pokhara University (Board)
b) Solve the difference equation:
$$u_{n+2} - 2\cos\alpha \, u_{n+1} + u_n = 0$$
by using Z-transform. **[7]**

```markdown
b) Solve $u_{n+2} - 2\cos\alpha\, u_{n+1} + u_n = 0$ using Z-transform. **[7]**
```

---

##### 🏛️ 2025 Spring — Pokhara University (Board)
a) Using Z-transform, solve the difference equation:
$$y_{n+2} + 6y_{n+1} + 9y_n = 2^n$$
with $y_0 = 0$, $y_1 = 0$. **[7]**

```markdown
a) Solve $y_{n+2} + 6y_{n+1} + 9y_n = 2^n$, $y_0 = y_1 = 0$, using Z-transform. **[7]**
```

---

##### 🏛️ 2024 Spring — Pokhara University (Board)
b) Solve the difference equation:
$$y_{n+2} - 7y_{n+1} + 12y_n = 2^n$$
with $y_0 = 0, y_1 = 0$ by using Z-transform. **[7]**

```markdown
b) Solve $y_{n+2} - 7y_{n+1} + 12y_n = 2^n$, $y_0 = y_1 = 0$, using Z-transform. **[7]**
```

---

##### 🏛️ 2024 Fall — Pokhara University (Board)
b) Solve the difference equation:
$$y_{n+2} - 7y_{n+1} + 12y_n = 2n$$
with $y_0 = 0$, $y_1 = 0$ by using Z-transform. **[8]**

```markdown
b) Solve $y_{n+2} - 7y_{n+1} + 12y_n = 2n$, $y_0 = y_1 = 0$, using Z-transform. **[8]**
```

---

##### 2024 Spring — Lumbini Engineering, Management & Science College / LEMSC (Final Internal)
b) Solve the difference equation using Z-transform:
$$y_{n+2} - 3y_{n+1} + 2y_n = 4^n$$
with $y_0 = 0$, $y_1 = 1$. **[7]**

```markdown
b) Solve $y_{n+2} - 3y_{n+1} + 2y_n = 4^n$, $y_0 = 0$, $y_1 = 1$. **[7]**
```

---

##### 2024 Spring — NAST (Pre-University)
b) Using Z-transform, solve the difference equation:
$$y_{n+2} + 3y_{n+1} + 2y_n = 0$$
with $y_0 = 0$, $y_1 = 1$. **[7]**

```markdown
b) Solve $y_{n+2} + 3y_{n+1} + 2y_n = 0$, $y_0 = 0$, $y_1 = 1$. **[7]**
```

---

##### 2024 Spring — NCIT (Assessment)
b) Solve the difference equation by using Z-transform:
$$y_{n+2} - 4y_{n+1} + 4y_n = 2^n$$
where $y_0 = 0$, $y_1 = 1$. **[8]**

```markdown
b) Solve $y_{n+2} - 4y_{n+1} + 4y_n = 2^n$, $y_0 = 0$, $y_1 = 1$. **[8]**
```

---

##### 2024 Spring — Nepal Engineering College / NEC (Assessment)
b) Using Z-transform, solve the difference equation:
$$y_{n+2} - 2y_{n+1} + y_n = 2^n$$
with $y_0 = 2$, $y_1 = 1$. **[7]**

```markdown
b) Solve $y_{n+2} - 2y_{n+1} + y_n = 2^n$, $y_0 = 2$, $y_1 = 1$. **[7]**
```

---

##### 2024 Spring — Madan Bhandari College of Engineering / MBCE (Final Internal)
b) Solve the difference equation by using Z-transform:
$$y_{n+2} - 4y_{n+1} + 4y_n = 2^n$$
with $y_0 = 0$, $y_1 = 1$. **[7]**

```markdown
b) Solve $y_{n+2} - 4y_{n+1} + 4y_n = 2^n$, $y_0 = 0$, $y_1 = 1$. **[7]**
```

---

##### 2024 Spring — Everest Engineering College (Pre-Board)
a) Solve the difference equation by using Z-transform:
$$y_{n+2} - 4y_{n+1} + 4y_n = 2^n$$
with $y_0 = 0$, $y_1 = 1$. **[7]**

```markdown
a) Solve $y_{n+2} - 4y_{n+1} + 4y_n = 2^n$, $y_0 = 0$, $y_1 = 1$. **[7]**
```

---

##### 2024 Spring — Pokhara Engineering College / PEC (Final Internal)
b) Solve the difference equation by using Z-transform:
$$y_{n+2} - 3y_{n+1} + 2y_n = 4^n$$
with $y_0 = 0$, $y_1 = 1$. **[8]**

```markdown
b) Solve $y_{n+2} - 3y_{n+1} + 2y_n = 4^n$, $y_0 = 0$, $y_1 = 1$. **[8]**
```

---

##### 2024 Spring — Universal Engineering & Science College / UESC (Pre-Board)
b) Solve the difference equation:
$$u_{n+2} - 2\cos\alpha \, u_{n+1} + u_n = 0$$
by using Z-transform. **[8]**

```markdown
b) Solve $u_{n+2} - 2\cos\alpha\, u_{n+1} + u_n = 0$ using Z-transform. **[8]**
```

---

##### 2024 Fall — United Technical College / UTC (Assessment)
a) Solve the difference equation:
$$y_{n+2} + 6y_{n+1} + 9y_n = 2^n$$
with $y_0 = 0$, $y_1 = 0$ by using Z-transform. **[8]**

```markdown
a) Solve $y_{n+2} + 6y_{n+1} + 9y_n = 2^n$, $y_0 = y_1 = 0$. **[8]**
```

---

##### 31 — Pokhara University (Affiliate)
b) Solve the difference equation:
$$y_{n+2} - 3y_{n+1} + 2y_n = 4^n$$
with $y_0 = 0$, $y_1 = 1$ by using Z-transform. **[7]**

```markdown
b) Solve $y_{n+2} - 3y_{n+1} + 2y_n = 4^n$, $y_0 = 0$, $y_1 = 1$. **[7]**
```

---

## Short Questions

##### 🏛️ 2025 Fall — Pokhara University (Board) — Q6a (any two × 5)
a) Find the Z-transform of $a^n \cos(bn)$.

```markdown
a) Find the Z-transform of $a^n \cos(bn)$.
```

---

##### 🏛️ 2024 Spring — Pokhara University (Board) — Q7b
b) Find $Z(a^n)$.

```markdown
b) Find $Z(a^n)$.
```

---

##### 🏛️ 2025 Spring — Pokhara University (Board) — Q7c
c) Find $Z(n^2)$.

```markdown
c) Find $Z(n^2)$.
```

---

##### 2024 Spring — Various papers
- Derive the formula for $Z(a^n)$. *(31 — PU)*
- Prove $Z(a^n) = \frac{z}{z-a}$. *(MBCE)*
- Find the Z-transform of $\sin(n\theta)$ and $\cos(n\theta)$. *(MBCE)*
- State and prove the Initial Value Theorem of Z-transform. *(Everest)*
- Find $Z(3n^2 - 2n + 1)$. *(Everest)*
- Find the Z-transform of $n a^n$. *(UESC, UTC)*
- Find $Z(a^n)$. *(NCIT)*
- Find the Z-transform of $n a^n$. *(NEC)*
- Find the Z-transform of the discrete unit impulse function $\delta(n)$. *(LEMSC)*
- Find $Z(e^{an})$. *(NAST)*
- State and prove the Initial Value Theorem of Z-transform. Find the inverse Z-transform of $F(z) = \frac{z^2+z}{z^2-2z+2}$. *(MBCE)*

```markdown
- Find $Z(a^n)$.
- Find the Z-transform of $\sin(n\theta)$ and $\cos(n\theta)$.
- State and prove the Initial Value Theorem of Z-transform.
- Find $Z(n^2)$.
```
