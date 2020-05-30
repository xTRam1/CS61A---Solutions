;Returns the sum of all the values in a list
(define (sum lst)
    (define (sum-track lst s)
        (if (null? lst) s (sum-track (cdr lst) (+ s (car lst))))
    )
    (sum-track lst 0)
)

;Reverses a list
(define (reverse lst)
    (define (reverse-sofar lst lst-sofar)
        (if (null? lst) lst-sofar 
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar))
        )
    )
    (reverse-sofar lst nil)
)

;Concatenates two lists together
(define (append a b)
    (define (rev-append-tail a b)
        (if (null? a) b
            (rev-append-tail (cdr a) (cons (car a) b))
        )
    )
    (rev-append-tail (reverse a) b)
)

;Takes in a number and a sorted list, inserts the number in the correct place 
;and return the list
(define (insert n lst)
    (define (rev-insert lst rev-lst)
        (cond
            ((null? lst) rev-lst)
            ((> (car lst) n) (rev-insert (cdr lst) (cons (car lst) rev-lst)))
            (else
                (rev-insert nil (append (reverse lst) (cons n rev-lst)))
            )
        )
    )
    (rev-insert (reverse lst) nil)
)