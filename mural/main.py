import random

def integer_input_request(text: str | None = None) -> str:
    var = input(f"Enter the {text}: ")
    while not var.isdigit():
        var = input(f"Enter the {text}. It must be an integer: ")
    return var


def max_beauty_score(line) -> int:
    # Since Thanh can paint only half of the sections, we need to find the contiguous subsequence
    # of length ⌈N/2⌉ with the highest possible sum to maximize the beauty score.

    scores = [int(score) for score in line]  # Create a list of integers from string
    N = len(line)

    l = (N + 1) // 2
    current_sum = sum(scores[:l])
    max_sum = current_sum  # Suppose that the answer is a subsequence starting from index 0

    for i in range(l, N):
        current_sum = current_sum - scores[i - l] + scores[i]  # The next iterated subsequence is
                                                               # shifted to the right by 1 section
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "main":
    T = int(integer_input_request("test cases quantity"))

    lines = []

    for i in range(T):
        N = int(integer_input_request("sections quantity"))

        sections_scores = integer_input_request("sections' beauty scores")
        while len(sections_scores) != N:
            print(f"There must be {N} scores")
            sections_scores = integer_input_request("sections' beauty scores")
        lines.append(sections_scores)

        # auto-testing
        #
        # N = random.randint(2, 100)
        # Ns.append(N)
        # lines.append(''.join(str(random.randint(0, 9)) for _ in range(N)))

    for i in range(T):
        print(f"Case #{i + 1}: {max_beauty_score(lines[i])}")