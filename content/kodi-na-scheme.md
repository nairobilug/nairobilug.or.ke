Title: Kodi na Scheme
Date: 2024-01-27 16:40
Category: Programming
Tags: linux, scheme, LambdaNative
Lang: sw
Slug: kodi-scheme
Author: Benson Muite
Summary: Tumia LambdaNative kutengeneza programu ya kuheasbu kodi

# Mwanzo

[LambdaNative](http://www.lambdanative.org/) inatumia
[Gambit Scheme](https://gambitscheme.org) kusaidia
mwandishi wa programu kuandika programu inaweza kutumikana kwa
simu na kompyuta.  Hapa, tutaonyesha mwandisho ya programu ndogo
ya kusaidia mtu kufanya hesabu ya kodi ya Kenya.  Maandiko hii
ni zoezi tu, tafadhali soma sheria za Kenya kujua kodi unahitaji
kulipa.

# Programu ya kwanza

Kuanza, ni nzuri kuandika programmu ndogo inaweza kutumikana
kwa kiweko kya kompyuta.

```
#!/usr/bin/gsi-script


(define relief 2400)
(define (getnhdf x)
  (* x 0.015))
(define (getshif x)
  (* x 0.0275))
(define (getnssf x)
  (cond ((<= x 18000) (* 0.06 x))
        (else 1080)))
(define (getpaye x)
  (cond ((<= x 0) 0)
        ((<= x 24000) (* 0.1 x))
        ((<= x 32334) (+ (* 0.25 (- x 24000)) 2400))
        ((<= x 500000) (+ (* 0.30 (- x 32334)) 2083.5 2400))
        ((<= x 800000) (+ (* 0.325 (- x 500000)) 140299.8 2083.5 2400))
        (else (+ (* 0.35 (- x 800000)) 105000.0  140299.8 2083.5 2400))))

(let ((monthly-salary (string->number (cadr (command-line)))))
  (display "Kodi zako ni:")
  (newline)
  (let ((nhdf (getnhdf monthly-salary)))
    (display "NHDF: ")
    (display nhdf)
    (newline)
    (let ((shif (getshif monthly-salary)))
      (display "SHIF: ")
      (display shif)
      (newline)
      (let ((nssf (getnssf monthly-salary)))
        (display "NSSF: ")
        (display nssf)
        (newline)
        (let ((taxable-salary 
                (cond ((<= (- monthly-salary nhdf shif nssf relief) 0) 0)
                      (else (- monthly-salary nhdf shif nssf relief)))))
          (display "Mshara unalipa PAYE: ")
          (display taxable-salary)
          (newline)
          (let ((paye (getpaye taxable-salary)))
            (display "PAYE: ")
            (display paye)
            (display "Mshahara mfukoni: ")
            (display (- monthly-salary paye nhdf shif nssf))
            (newline)))))))
```

Kutumia programu hii, sakinisha [Gambit Scheme](https://gambitscheme.org/latest/) kwa
kompyuta yako. Hifadhi programu kwa faili inaitwa `kodi.scm`.  Halafo kwa kiweko
chapisha:
```
gsi-scheme kodi.scm 20000
```
Nambari ya mwisho ni mshahara inapatikana kila mwezi unataka kujua kodi.
Scheme zingine zinaweza kutumikana pia, lakini, kuzitumia, badili laini za kichwa.
Kwa mfano, ukitaka kutumia [Guile](https://www.gnu.org/software/guile/), tumia
```
#!/usr/bin/guile -s
!#
```
kwa laini ya kwanza na ya pili.  



*Maandiko hizi zina leseni ya [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
*Programu zina leseni ya [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)*
