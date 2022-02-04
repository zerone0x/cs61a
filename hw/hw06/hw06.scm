(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))


(define (caddr s)
  (car (cdr (cdr s))))


(define (sign num)
  (cond ((= num 0) 0)
  ((> num 0) 1)
  ((< num 0) -1)))


(define (square x) (* x x))

(define (pow x y)
  (cond 
  ((= y 0) 1)
  ((= x 1) 1)
  ((= 1 (modulo y 2)) (* x (pow x (/ (- y 1) 2)) (pow x (/ (- y 1) 2))))
  (else (* (pow x (/ y 2)) (pow x (/ y 2))))))

  '该抽象出square