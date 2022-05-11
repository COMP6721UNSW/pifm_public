def fits(context: Context, l: int, h: int) -> int:
    requires("fits_bounds", 0 <= l < h <= context.NUM_WORDS)

def cost(context: Context, l: int, h: int) -> float:
    requires("cost_fits", fits(context, l, h))


def overall_cost(context: Context, costs: List[int], n: int, i: int) -> float:
    requires("overall_cost_bounds", 0 <= n < i)
    requires("overall_cost_fits", fits(context, n, i))

def get_minimum_costs(context, costs):
    holds_invariant("costs_correct", costs_are_correct(costs, n))
    holds_invariant("ci_minimum", ci_is_minimum(ci, n, i))

def get_word_lengths_per_line(context, costs, word_lengths):
    holds_invariant("word_lengths_ok", word_lengths == flatten_list(word_lengths_per_line) + word_lengths[n:])
    holds_invariant("costs_ok", costs[n] <= costs[0] if n < context.NUM_WORDS else True)
    holds_invariant("cost_lte_first_cost", cost_of_line_is_lte_first_cost(costs, word_lengths_per_line))
    holds_invariant("word_length_fits", fits(context, n, i))

def make_line(context, ls, b):
    requires("make_line_b_ok", b >= 0)
    requires("make_line_ls_ok", ls != [])
