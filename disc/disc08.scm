;Returns the factorial of a function
(define (factorial x)
	(cond
		((= x 1) 1)	
		((* x (factorial (- x 1))))
	)
)

;Returns the nth fibonacci number
(define (fibonacci n)
	(cond
		((= n 1) 1)
		((= n 0) 0)
		(else
			(+ (fibonacci (- n 1)) (fibonacci (- n 2)))
		)
	)
)

;Concatenates two list
(define (concat a b)
	(cond
		((null? a) b)
		(else
			(cons (car a) (concat (cdr a) b))
		)
	)
)

;Returns a list where x is repeated n times
(define (replicate x n) 
	(cond
		((= n 0) nil)
		(else
			(cons x (replicate x (- n 1)))
		)
	)
)

;Takes a compressed sequence and expands it into its original sequence
(define (uncompress s)
	(cond
		((null? s) nil)
		(
			(define value (car (car s)))
			(define times (car (cdr (car s))))
			(concat (replicate value times) (uncompress (cdr s)))
		)
	)
)

;Applies a procedure to every element of a list
(define (map fn lst)
	(cond
		((null? lst) nil)
		(else
			(cons (fn (car lst)) (map fn (cdr lst)))
		)
	)
)

;Applies a procedure to every element in a nested list
(define (deep-map fn lst)
	(cond
		((null? lst) nil)
		((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))) 
		(else
			(cons (fn (car lst)) (deep-map fn (cdr lst)))
		)
	)
)

;EXTRA

;Abstract Data Type : Tree
(define (make-tree label branches) (cons label branches))

;Gets the lable of a Tree
(define (label tree) (car tree))

;Gets the branches of a Tree
(define (branches tree) (cdr tree))

;Sums all of the entries of a tree
(define (tree-sum tree)
	;Takes the sum of the elements of a list
	(define (helper lst sum) 
		(cond
			((null? lst) sum)
			(else
				(helper (cdr lst) (+ sum (car lst)))
			)
		)
	)
)

;creates a new tree where the entries are the product of the 
;entries along the path to the root in the original tree.
(define (path-product-tree t)
	(define (product-tracker t product)
		(cond
			((null? t) nil)
			((list? (label t)) (cons (product-tracker (label t) product) (product-tracker (branches t) product)))
			(else
				(cons (* (label t) product) (product-tracker (cdr t) (* product (label t))))
			)	
		)
	)
	(product-tracker t 1)
)




