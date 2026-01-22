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

## Tumia LambdaNative Kutengeneza Kiolesura cha Mtumiaji

```
;; Display variables
(define gui #f)
(define kodi-subdisplay1 #f)
(define kodi-subdisplay2 #f)
(define kodi-subdisplay3 #f)
(define kodi-subdisplay4 #f)
(define kodi-display #f)
(define kodi-introdisplay #f)
(define start-button #f)

(define keypad `((
  ( #\7 #\8 #\9 )
  ( #\4 #\5 #\6 )
  ( #\1 #\2 #\3 )
  ( #\0 (#\h "Hesabu") (#\f "Futa"))
)))

;; State
(define Hesabu #f)
;; Tax relief
(define relief 2400)
(define paye 0)
(define nssf 0)
(define shif 0)
(define mshahara-mfukoni 0)
(define mshahara 0)

;; Tax calculations
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

;; Clear displays
(define (kodi-futa)
  (glgui-widget-set! gui kodi-subdisplay1 'label "")
  (glgui-widget-set! gui kodi-subdisplay2 'label "")
  (glgui-widget-set! gui kodi-subdisplay3 'label "")
  (glgui-widget-set! gui kodi-subdisplay4 'label "")
  (glgui-widget-set! gui kodi-display 'label "")
  (set! Hesabu #f))

;; Calculate taxes, check input is not void
(define (kodi-hesabu)
    (let* ((mshahara-str (glgui-widget-get gui kodi-display 'label))
           (evalstr (string-append "\\" mshahara-str ";"))
           (res (with-input-from-string evalstr (lambda ()
            (with-exception-catcher (lambda (mshahara-str) #f) (lambda () (eval (read))))))))
        (set! Hesabu (if (eq? res (void)) #f res))
        (if Hesabu
          (set! mshahara (string->number mshahara-str)))
        (set! shif (getshif mshahara))
        (set! nssf (getnssf mshahara))
        (set! mshahara-wa-kodi
             (cond ((<= (- mshahara shif nssf relief) 0) 0)
                    (else (- mshahara shif nssf relief))))
        (set! paye (getpaye mshahara-wa-kodi))
        (set! mshahara-mfukoni (- mshahara paye shif nssf))
        (if Hesabu
           (kodi-updatesub))
        (set! Hesabu #f)))

;; Display upto 2 decimal places
(define (number->currency n)
  (number->string (/ (round (* 100 n)) 100)))

;; Update displays
(define (kodi-updatesub)
    (glgui-widget-set! gui kodi-subdisplay1 'label
      (string-append "PAYE " (if Hesabu (number->currency paye) "")))
    (glgui-widget-set! gui kodi-subdisplay2 'label
      (string-append "NSSF " (if Hesabu (number->currency nssf) "")))
    (glgui-widget-set! gui kodi-subdisplay3 'label
      (string-append "SHIF " (if Hesabu (number->currency shif) "")))
    (glgui-widget-set! gui kodi-subdisplay4 'label
      (string-append "Pesa Mfukoni " (if Hesabu (number->currency mshahara-mfukoni) ""))))

(main
;; initialization
  (lambda (w h)
    (make-window 320 480)
    (glgui-orientation-set! GUI_PORTRAIT)
    (set! gui (make-glgui))
    (let* ((w (glgui-width-get))
           (h (glgui-height-get)))
      (set! kodi-subdisplay1 (glgui-label gui 0 (- h 50) w 20 "" ascii_18.fnt LightBlue))
      (glgui-widget-set! gui kodi-subdisplay1 'align GUI_ALIGNLEFT)
      (glgui-widget-set! gui kodi-subdisplay1 'hidden #t)
      (set! kodi-subdisplay2 (glgui-label gui 0 (- h 70) w 20 "" ascii_18.fnt Yellow))
      (glgui-widget-set! gui kodi-subdisplay2 'align GUI_ALIGNLEFT)
      (glgui-widget-set! gui kodi-subdisplay2 'hidden #t)
      (set! kodi-subdisplay3 (glgui-label gui 0 (- h 90) w 20 "" ascii_18.fnt LightGreen))
      (glgui-widget-set! gui kodi-subdisplay3 'align GUI_ALIGNLEFT)
      (glgui-widget-set! gui kodi-subdisplay3 'hidden #t)
      (set! kodi-subdisplay4 (glgui-label gui 0 (- h 110) w 20 "" ascii_24.fnt Orange))
      (glgui-widget-set! gui kodi-subdisplay4 'align GUI_ALIGNLEFT)
      (glgui-widget-set! gui kodi-subdisplay4 'hidden #t)
      (set! kodi-introdisplay (glgui-label gui 5 (- h 80) (- w 10) 60 "Hesabu Kodi" ascii_32.fnt Green))
      (glgui-widget-set! gui kodi-introdisplay 'align GUI_ALIGNCENTER)
      (glgui-widget-set! gui kodi-introdisplay 'hidden #f)
      (set! kodi-display (glgui-label gui 5 (- h 30) (- w 10) 0 "" ascii_32.fnt White))
      (glgui-widget-set! gui kodi-display 'align GUI_ALIGNRIGHT)
      (glgui-widget-set! gui kodi-display 'focus #t)
      (glgui-widget-set! gui kodi-display 'hidden #t)
      (set! start-button
        (glgui-button-string gui (+ 5 (/ w 3) 5) (- h 44 150) 75 25 "ANZA" ascii_24.fnt
          (lambda (g . x)
            (glgui-widget-set! gui kodi-introdisplay 'hidden #t)
            (glgui-widget-set! gui start-button 'hidden #t)
            (glgui-widget-set! gui kodi-subdisplay1 'hidden #f)
            (glgui-widget-set! gui kodi-subdisplay2 'hidden #f)
            (glgui-widget-set! gui kodi-subdisplay3 'hidden #f)
            (glgui-widget-set! gui kodi-subdisplay4 'hidden #f)
            (glgui-widget-set! gui kodi-display 'hidden #f)
            (let ((wgt (glgui-keypad gui 5 5 (- w 10) (- h 130 5) ascii_24.fnt keypad)))
              (glgui-widget-set! gui wgt 'rounded #f)
              (glgui-widget-set! gui wgt 'floatinghighlight #f)))))
      (glgui-widget-set! gui start-button 'color Red)
    ))

;; events
  (lambda (t x y)
    (let ((skipevent #f))
      (if (= t EVENT_KEYRELEASE)
        (cond
          ((= x EVENT_KEYESCAPE)     (terminate))
          ((= x (char->integer #\h)) (kodi-hesabu) (set! skipevent #t))
          ((= x (char->integer #\f)) (kodi-futa) (set! skipevent #t))
        ))
      (if (not skipevent) (glgui-event gui t x y))))

;; termination
  (lambda () #t)
;; suspend
  (lambda () (glgui-suspend) (terminate))
;; resume
  (lambda () (glgui-resume))
)

;; eof

```

*Maandiko hizi zina leseni ya [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*
*Programu zina leseni ya [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.txt)*
