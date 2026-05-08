const Pagination = () => {

  return (

    <div className="flex items-center justify-between mt-6">

      <p className="text-sm text-gray-500">
        Showing 1 to 10 of 100 entries
      </p>

      <div className="flex gap-2">

        <button className="px-4 py-2 border rounded-lg">
          Previous
        </button>

        <button className="px-4 py-2 bg-blue-600 text-white rounded-lg">
          1
        </button>

        <button className="px-4 py-2 border rounded-lg">
          2
        </button>

        <button className="px-4 py-2 border rounded-lg">
          Next
        </button>

      </div>

    </div>

  );

};

export default Pagination;