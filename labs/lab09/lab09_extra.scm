;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
)

(define f (lambda (x) (* x 2)))
(define g (lambda (x) (* x x)))

; Q6
(define (composed f g)
  (define (embedded x)
  	(f (g x))
  )
  embedded
)

; Q7
(define (remove item lst)
  (cond 
  	((null? lst) nil)
  	((= (car lst) item) (remove item (cdr lst)))
  	(else (cons (car lst) (remove item (cdr lst))))
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
  (cond
  	((null? s) nil)
  	(else 
  		(define added-one (car s))
  		(define s (remove added-one s))
  		(cons added-one (no-repeats s))
  	)
  )
)

; Q9
(define (substitute s old new)
  (cond
  	((null? s) nil)
  	((eq? (car s) old) (cons new (substitute (cdr s) old new)))
  	((not (eq? (car s) old))(cons (car s) (substitute (cdr s) old new)))
  )
)

; Q10
(define (sub-all s olds news)
  
)

