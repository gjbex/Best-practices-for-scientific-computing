# Syntax versus semantics

"Syntax" and "semantics" are two terms we will use often in this training. Most
of you are probably familiar with these concepts, but just to make sure, let's
define them briefly.

The syntax of a programming language is its grammar, i.e., the rules the source
code text must satisfy in order to be considered syntactically correct. Let's
illustrate that with an example from natural language. The sentence "the dog
barks" is syntactically correct, while "the dog bark" is not.

Semantics on the other hand has to do with meaning, or interpretation. Again
drawing on natural language examples, the sentence "the dog spoke" is
syntactically correct, but the semantics is wrong. Obviously, dogs do not speak,
except in fairy tales. The sentence "the dog barks" is both syntactically and
semantically correct.

The following code fragments would be syntactically incorrect.

~~~~fortran
program syntax_error
    implicit none
    use, intrinsic :: iso_fortran_env, only : output_unit
    write (unit=output_unit, fmt='(A)') 'hello world'
end program syntax_error
~~~~

This Fortran program has a syntax error that is dutifully reported by the
`gfortran` compiler as:

~~~bash
$ gfortran -c syntax_error.f90
syntax_error.f90:3.57:

    use, intrinsic :: iso_fortran_env, only : output_unit
                                                         1
syntax_error.f90:2.17:

    implicit none
                 2
Error: USE statement at (1) cannot follow IMPLICIT NONE statement at (2)
~~~~

The following Fortran function definition has a semantic error, although it is
syntactically correct.

~~~~fortran
integer function fac(n)
    implicit none
    integer, intent(IN) :: n
    integer :: i
    fac = 1
    do i = 0, n
        fac = fac*i
    end do
end function fac
~~~~

The code fragment above will be compiled without errors or even warnings, but
the function will return zero when invoked, regardless of the argument passed
to it.

This illustrates an important point: syntax errors are always caught by the
compiler. Although having to fix syntax errors is a nuisance, it is relatively
easy.

Most semantic errors are not caught by the compiler, so these are harder to spot
and more difficult to fix. Compilers do offer some help detecting certain
classes of semantic error, as you can see in the Tools section.
