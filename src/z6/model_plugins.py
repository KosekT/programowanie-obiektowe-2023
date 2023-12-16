from model import *


class SimpleProblem(Problem):

    def render(self) -> bytes:
        # todo: wyświetlić ładnie pytanie na konsoli (razem z treściami odpowiedzi)
        pass

    def parse(self, text_lines: Iterable[str]) -> 'Problem':
        # proper parse error exceptions (raises ParseError)
        """
        Whole test is given by a file with the following format:

        ```
        # duration_min, n_problems_per_test
        5 ;; 2
        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        ---
        TEXT: Następujące informacje nt. stolic są prawdziwe
        Q: Stolicą Rwandy jest Kigali ;; N ;; 2 ;; 0
        Q: Stolicą Irlandii jest Dublin ;; Y ;; 1 ;; -1

        # - linie zaczynajace się od # są komentarzami
        # - pierwsza linia to konfiguracja testu
        # - kolejne sekcje (oddzielone przez '---') są problemami (Problem)
        # - TEXT jest tekstem problemu
        # - linie zaczynające się od Q: to pytania
        # - każda z linii pytań zawiera, oddzielone przez ;; następujące dane:
        #     - tekst pytnia
        #     - czy należy na pytanie odpowiedzieć przez 'Y' czy 'N'
        #     - jaka jest wartosc poprawnej odpowiedzi
        #     - jaka jest wartosć niepoprawnej odpowiedzi
        ```

        """
        problem = SimpleProblem()
        return problem
