;Takes in two lists and makes a larger list
(define (append lst1 lst2)
	(cond
		((null? lst1) lst2)
		(else
			(cons (car lst1) (append (cdr lst1) lst2))
		)
	)
)

;Reverses a list
(define (reverse-with-append lst)
	(cond
		((null? (cdr lst)) (list (car lst)))
		(else
			(append (reverse (cdr lst)) (list (car lst)))
		)
	)
)

;Reverse without append
(define (reverse lst)
	(define (helper lst curr)
		(cond
			((null? (cdr lst)) curr)
			(else
				(helper (cdr lst) (cons (car (cdr lst)) curr))
			)
		)
	)
	(helper lst (cons (car lst) nil))
)

;Adds a word to the beginning of every sub list
(define (add-to-all word lst)
	(cond
		((null? lst) nil)
		(else
			(cons (cons word (car lst)) (add-to-all word (cdr lst)))
		)
	)
)

;Applies fn to every element of the list
(define (map fn lst)
	(if (null? lst) nil
		(cons (fn (car lst)) (map fn (cdr lst)))
	)
)

;add-to-all procedure using the map procedure
(define (add-to-all word lst)
	(map (lambda (x) (cons word x)) lst)
)

;Returns the sub-lists of a list
(define (sub-lists lst)
	(cond
		((null? lst) (cons nil nil))
		(else 
			(define sub-list (sub-lists (cdr lst)))
			(define added (add-to-all (car lst) sub-list))
			(append sub-list added)
		)
	)
)


;Returns the number of times 1 follows 6 in a list
(define (sixty-ones lst)
	(cond
		((null? lst) 0)
		((and (= (car lst) 6) (= (car (cdr lst)) 1)) (+ 1 (sixty-ones (cdr lst))))
		(else
			(sixty-ones (cdr lst))
		)
	)
)

;Return a list of all distinct length-n lists of 1s and 6s that do not 
;contain after 1




