var unsorted_array;
var sorted_array;
var GLOBAL_GRAPH;
const GLOBAL_COLOR = "crimson";
const bar = "bar";
const line = "line";

// Hash map to store the algorithm name
const ALGORITHMS = {
  1: "Bubble sort",
  2: "Selection sort",
  3: "Insertion sort",
  4: "Merge sort",
  5: "Heap_sort",
  6: "Quick sort single pivot",
  7: "Quick sort three medians",
};

/*
Function generate() is responsible to check the user inputs on the GUI and arrange in it in a format for the next functions.
It is also responsible to clear up the earlier graphs and data associated with the previous selections.
*/
function generate() {
  document.getElementById('show').hidden = true;

  const val = parseInt(document.getElementById("val").value);
  const custom_val = [];
  document
    .getElementById("val_custom")
    .value.split(", ")
    .forEach((element) => {
      custom_val.push(parseInt(element));
    });

  if (GLOBAL_GRAPH) {
    GLOBAL_GRAPH.destroy();
  }
  const func_array = [];

  for (var i = 1; i < 8; i++) {
    const c = document.getElementById(${i}).checked;
    if (c === true) {
      func_array.push(i);
    }
    if (i === 7) {
      if (func_array.length === 0) {
        document.getElementById("compare_chart").hidden = true;
        document.getElementById("hide_chart").hidden = false;
      }
      if (func_array.length === 1) {
        single_chart(val, func_array[0], custom_val);
      } else if (func_array.length > 1) {
        compare_chart(val, func_array, custom_val);
      }
    }
  }
}

/*
Function compare_chart generates a graph for comparison of the sorting algorithms selected by the user
This function makes use of the Python Eel APIs to get an array generated from the Backend
The generated arrays are then further sent back to Backend to be sorted
*/
function compare_chart(val, func_array, custom_val) {
  eel.array_generator(
    val,
    0
  )(function (res) {
    custom_val = custom_val.filter(element => !Number.isNaN(element))
    unsorted_array = custom_val.length > 0 ? custom_val : res;

    eel.sorting_algorithm(
      func_array,
      unsorted_array,
      1
    )(function (res) {
      var time = [];
      var name = [];
      var label =
        "Execution Time (sec) (Y-Axis) Vs. Array Length " +
        unsorted_array.length.toString();
      sorted_array = res[1];
      res[0].forEach((element) => {
        time.push(element[0]);
        name.push(ALGORITHMS[element[2]]);
      });
      generate_graph(time, label, name, GLOBAL_COLOR, bar, 'Sorting Algorithms');
      document.getElementById("compare_chart").hidden = false;
      document.getElementById("hide_chart").hidden = true;
    });
  });
}

/*
This function generates graph for single algorithms.
It receives multiple arrays with different length from the backend and sorts it using the single function
*/
function single_chart(val, func, custom_val) {
  eel.array_generator(
    val,
    1
  )(function (res) {
    custom_val = custom_val.filter(element => !Number.isNaN(element))
    var single_custom_val = [[0]]
    single_custom_val.push(custom_val)
    if (custom_val.length > 0) {
      unsorted_array =  single_custom_val
      document.getElementById('show').hidden = false;
    }
    else {
      unsorted_array = res
    }

    eel.sorting_algorithm(
      func,
      unsorted_array,
      0
    )(function (res) {
      var time = [];
      var length = [];
      const label =
        "Execution time (sec) (Y-Axis) Vs Array Length (X-Axis) for " +
        ALGORITHMS[func];
      sorted_array = res[1];
      res[0].forEach((element) => {
        length.push(element[0]);
        time.push(element[1]);
      });
      const type = custom_val.length > 0 ? bar : line
 
      generate_graph(time, label, length, GLOBAL_COLOR, line, 'Length of Arrays');
      document.getElementById("compare_chart").hidden = false;
      document.getElementById("hide_chart").hidden = true;
    });
  });
}