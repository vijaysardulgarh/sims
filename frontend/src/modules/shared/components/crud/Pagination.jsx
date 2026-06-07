const Pagination = ({
  currentPage,
  totalPages,
  onPageChange,
}) => {

  return (

    <div className="flex flex-col md:flex-row items-center justify-between mt-6 gap-4">

      {/* PAGE INFO */}
      <p className="text-sm text-gray-500">

        Page {currentPage} of {totalPages}

      </p>

      {/* BUTTONS */}
      <div className="flex gap-2">

        {/* PREVIOUS */}
        <button
          onClick={() =>
            onPageChange(currentPage - 1)
          }
          disabled={currentPage === 1}
          className="px-4 py-2 border rounded-lg disabled:opacity-50"
        >
          Previous
        </button>

        {/* CURRENT PAGE */}
        <button
          className="px-4 py-2 bg-blue-600 text-white rounded-lg"
        >
          {currentPage}
        </button>

        {/* NEXT */}
        <button
          onClick={() =>
            onPageChange(currentPage + 1)
          }
          disabled={
            currentPage === totalPages
          }
          className="px-4 py-2 border rounded-lg disabled:opacity-50"
        >
          Next
        </button>

      </div>

    </div>

  );

};

export default Pagination;