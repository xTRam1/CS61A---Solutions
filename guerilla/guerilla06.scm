;Returns an infinite stream containing all elements from both
;streams in sorted order
(define (merge s1 s2)
    (cond
        ((>= (car s1) (car s2)) (cons-stream (car s2) (merge (cdr-stream s1) (cdr-strema s2))))
        ((>= (car s2) (car s1)) (cons-stream (car s1) (merge (cdr-stream s1) (cdr-stream s2))))
    )
)

;Gives an infinite list of naturals numbers starting from a numbers
(define (naturals start)
    (cons-stream start (naturals (+ start 1)))
)

;Return the sum of the first k elements that satisfy f
(define (sum-satisfied-k lst f k)
    (define (helper lst f k sum)
        (cond
            ((and (null? lst) (> k 0)) 0)
            ((= k 0) sum)
            ((f (car lst)) (helper (cdr lst) f (- k 1) (+ sum (car lst))))
            (else
                (helper (cdr lst) f k sum)
            )
        )
    )
    (helper lst f k 0)
)