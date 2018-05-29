#lang racket

(define p
  (lambda (s)
    (if (= (list-ref s 0) '1)
        (= (count (curry equal? '1) s) (count (curry equal? '0) s))
        false)))