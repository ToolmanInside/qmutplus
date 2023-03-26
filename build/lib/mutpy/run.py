from commandline import run_mutpy
from mutpy.test_runners import UnittestTestRunner
from controller import MutationController
from utils import ModulesLoader
import operators
import controller
import views

TARGET = [
    '/Users/think/qmutplus/adder_04.py',
    '/Users/think/qmutplus/bv_04.py',
    ]
UNITTEST = [
    '/Users/think/qmutplus/test_adder_04.py',
    '/Users/think/qmutplus/test_bv_04.py',
    ]

# output views
QUIET = False
REPORT = False # output YAML report
HTML_REPORT = False # output HTML report
DEBUG = False # debug view
SHOW_MUTANT = False
COLORED_OUTPUT = False

def get_runner_cls():
    return UnittestTestRunner

def build_name_to_operator_map():
    result = {}
    for operator in operators.standard_operators | operators.experimental_operators:
        result[operator.name()] = operator
        result[operator.long_name()] = operator
    return result

def build_mutator():
    operators_set = set()
    name_to_operator = build_name_to_operator_map()
    operators_set.add(name_to_operator['QGR'])
    operators_set.add(name_to_operator['QGD'])
    operators_set.add(name_to_operator['QMD'])
    # operators_set.add(name_to_operator['QGI'])
    # operators_set.add(name_to_operator['QMI'])
    return controller.FirstOrderMutator(operators_set, 100)

def build_views(output_file_name = None):
    views_list = []
    if QUIET:
        views_list.append(views.QuietTextView(COLORED_OUTPUT))
    else:
        views_list.append(views.TextView(COLORED_OUTPUT, SHOW_MUTANT))
    if REPORT:
        views_list.append(views.YAMLReportView(output_file_name))
    if HTML_REPORT:
        views_list.append(views.HTMLReportView(output_file_name))
    if DEBUG:
        views_list.append(views.DebugView())
    return views_list

def main():
    ctler = MutationController(
        runner_cls = get_runner_cls(),
        target_loader = ModulesLoader(TARGET, '..'),
        test_loader = ModulesLoader(UNITTEST, '..'),
        views=build_views(),
        mutant_generator=build_mutator(),
        timeout_factor=5,
    )
    ctler.run()

if __name__ == "__main__":
    main()
