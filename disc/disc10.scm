;Returns a parameter-less lambda procedure
(define-macro (make-lambda expr) (list 'lambda nil expr))

;Takes two expressions together and or's them together
(define-macro (or-macro expr1 expr2) 
    `(let ((v1 ,expr1)) 
        (if v1 v1 ,expr2)
    )
)

;Returns a stream consisting of integers in a given range
(define (range-stream start end)
    (if (= start end) nil
        (cons-stream start (range-stream (+ start 1) end))
    )
)

;Slices a stream and returns a Scheme list
(define (slice s start end)
    (cond
        ((or (null? s) (= end 0)) nil)
        ((> start 0) (slice (cdr-stream s) (- start 1) (- end 1)))
        ((= start 0) (cons (car s) (slice (cdr-stream s) start (- end 1))))
    )
)

;Gives an infinite list of naturals numbers starting from a numbers
(define (naturals start)
    (cons-stream start (naturals (+ start 1)))
)

(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys))
    nil
    (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))

;;;;;;;;;;;;;;;;
;EXAM PREP 07;;;
;;;;;;;;;;;;;;;;

;Reverses a list
(define (reverse lst)
    (define (f l r)
        (if (null? l) r
            (f (cdr l) (cons (car l) r))
        )
    )
    (f lst nil)
)

;Raises b to the nth power
(define (power b n)
    (define (helper power so-far)
        (if (= power 0) so-far
            (helper (- power 1) (* so-far b))
        )
    )
    (helper n 1)
)

;Finds the lenght of the hailstone sequence that starts with n
(define (hailstone n)
    (define (helper k i)
        (if (= k 1) i
            (if (= (modulo k 2) 0) (helper (/ k 2) (+ 1 i))
                (helper (+ (* k 3) 1) (+ 1 i))
            )
        )
    )
    (helper n 1)
)

;;;;;;;;;;;;;;;;
;EXAM PREP 08;;;
;;;;;;;;;;;;;;;;

;Checks if a list contains a value
(define (contains value lst)
    (cond
        ((null? lst) #f)
        ((eq? (car lst) value) #t)
        (else
            (contains value (cdr lst))
        )
    )
)

;A special form which checks if the value is in one of the lists
;returns a result accordingly
(define-macro (case value clause)
    `(cond
            ((contains ,value ,(car (car clause))) ,(car (cdr (car clause))))
            ((contains ,value ,(car (car (cdr clause)))) ,(car (cdr (car (cdr clause)))))
            (else ,(car (cdr (car (cdr (cdr clause))))))  
    )
)
