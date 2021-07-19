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
        # return "<div '> Hello </div>"
        try:
            arr = [int(i) for i in arr]
            root = traversal(TreeNode(arr))
            lll = levelOrderTraversal(root)
            final = []
            # print(lll)
            pfa = processFinalArray(mergeTree(root, final))
            string1 = ""
            string2 = ""
            # print(pfa)
            # string1 += "<div style='padding: 2rem; width: 2rem; border: 2px solid black; height: 2rem;'>" + \
            #     "hello" + "</div>"
            for fa in lll:
                string2 += "<div style='display: flex; flex-direction: row; align-items: center; justify-content: center;'>"
                for x in fa:
                    string2 += "<span style='padding: .5rem; width: auto; border: 2px solid black; height: 2rem; margin-left: 2rem;'>" + \
                        str(x) + "</span>"
                string2 += "</div> <br/>"
            for fa in pfa:
                string1 += "<div style='display: flex; flex-direction: row; align-items: center; justify-content: center;'>"
                for x in fa:
                    string1 += "<span style='padding: .5rem; width: auto; border: 2px solid black; height: 2rem; margin-left: 2rem;'>" + \
                        str(x) + "</span>"
                string1 += "</div> <br/>"
            return string2 + string1
        except Exception as e:
            return e

    return render_template(
        'index.html',
        title="Merge Sort visualizer",
        description="get a unsorted array from user as an input and display how merge sort sorts the array behind the scenes",
    )


if __name__ == '__main__':

    app.run(debug=True)
