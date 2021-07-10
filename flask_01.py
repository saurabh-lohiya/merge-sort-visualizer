from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask import request
from main import mergeSort, levelOrderTraversal, traversal, mergeTree, TreeNode, processFinalArray
# from split import validation

app = Flask(__name__,
            template_folder='templates',
            static_folder="static",
            instance_relative_config=False)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_array = request.form.get("list_of_numbers")
        arr = input_array.split(",")
        try:
            arr = [int(i) for i in arr]
            root = traversal(TreeNode(arr))
            lll = levelOrderTraversal(root)
            final = []
            pfa = processFinalArray(mergeTree(root, final))
            string1 = ""
            string2 = ""
            print(pfa)
            for fa in lll:
                for x in fa:
                    string2 += str(x)
                string2 += "<br/>"
            for fa in pfa:
                for x in fa:
                    string1 += str(x)
                string1 += "<br />"
            return string1 + "<br/>" + string2
        except Exception as e:
            return e

    return render_template(
        'index.html',
        title="Merge Sort visualizer",
        description="get a unsorted array from user as an input and display how merge sort sorts the array behind the scenes",
    )


if __name__ == '__main__':

    app.run(debug=True)
