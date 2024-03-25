Require Import Utf8.
Require Import Classical.

Variables p q:Prop.
Variables U:Type.
Variables P Q T: U → Prop.
Variables f : U → U.

Example a: ¬¬(p ∧ q) → ¬¬p ∧ ¬¬q.
Proof.
unfold not.
intros.
split.
- intros.
  apply H.
  intros.
  destruct H1.
  apply H0.
  assumption.
- intros.
  apply H.
  intros.
  destruct H1.
  apply H0.
  assumption.
Qed.

Example b: (∀ x:U, P(x) ∨ Q(f(x))) ∧
                    (∀ x:U, T(f(x)) → ¬ P(x)) ∧
                    (∃ x:U, T(f(x)))
                    → (∃ x:U, Q(f(x))).
Proof.
intros.
destruct H.
destruct H0.
destruct H1.
assert (¬P(x)).
- apply H0.
  assumption.
- exists x.
  assert (P(x) ∨ Q(f(x))). apply H.
  destruct H3.
  + contradiction.
  + assumption.
Qed.

Example c: (p → q) ∨ (q → p).
Proof.
assert (p ∨ ¬p).
apply classic.
destruct H.
- right.
  intros.
  assumption.
- left.
  intros.
  contradiction.
Qed.

