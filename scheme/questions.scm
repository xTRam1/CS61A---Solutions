(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests)
)

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (enu-helper s n)
    (cond 
      ((null? s) nil)
      (else
        (cons (list n (car s)) (enu-helper (cdr s) (+ n 1)))
      )
    )
  )
  (enu-helper s 0)
)
; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((= total 0) (cons nil nil))
    ((< (- total (car denoms)) 0) (list-change total (cdr denoms)))
    (else
      (define with-first-denom (list-change (- total (car denoms)) denoms))
      (define with-others (list-change total (cdr denoms)))
      (append (cons-all (car denoms) with-first-denom) with-others)
    )
  )
)

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr) expr)
        ((quoted? expr) expr)
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
              (append (list form params) (map let-to-lambda body))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
              (define pairs (zip values))
              (define params (car pairs))
              (define args (map let-to-lambda (cadr pairs)))
              (define body (map let-to-lambda body))
              (cons (append (list 'lambda params) body) args)
           ))
        (else
              (map let-to-lambda expr)
         )))
