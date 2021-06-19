from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask import request
from main import mergeSort
# from split import validation

app = Flask(__name__,
            template_folder='templates',
            static_folder="static",
            instance_relative_config=False)


# assets = Environment(app)
# assets.url = app.static_url_path
# scss = Bundle('./template/index.scss', filters='pyscss',
#               output='./template/index.css')
# assets.register('scss_all', scss)

# decorator

# hi
[1, 2, 3]
{
    {

    }
}


@app.route('/', methods=["GET", "POST"])
def index():
    # string1 = "<p>Merge Sort Equalizer</p>"
    # string2 = "<br/>"
    # stringn = mergeSort([1, 4, 1, 2])
    # string3 = "<p>Enter Comma seperated Numbers</p>"
    # string4 = '<input type='"textbox"' size='"50"'></input>'
    # string5 = "<br/>"
    # string6 = '<input type='"submit"'>'
    # return string1 + string2 + str(stringn) + string3 + string4 + string5 + string6
    if request.method == "POST":
        input_array = request.form.get("list_of_numbers")
        arr = input_array.split(",")
        try:
            arr = [int(i) for i in arr]
            arr = mergeSort(arr)
            x = [str(i) for i in arr]
            return " ".join(x)
        except:
            return render_template('alert.html')
        return "".join(x)
        # return mergeSort(validation(input_array))
    # else:
    return render_template(
        'index.html',
        title="Merge Sort visualizer",
        description="get a unsorted array from user as an input and display how merge sort sorts the array behind the scenes",
    )


if __name__ == '__main__':

    app.run(debug=True)
