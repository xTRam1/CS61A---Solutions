
;List comphrenesion loop in Scheme!!!!
(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) (if ,filter-expr ,map-expr)) ,lst))
)
