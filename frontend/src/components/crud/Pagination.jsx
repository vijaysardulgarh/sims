import React from "react";

const Pagination = ({
    currentPage,
    totalPages,
    onPageChange,
}) => {

    return (
        <div className="flex items-center gap-2">

            <button
                disabled={currentPage === 1}
                onClick={() =>
                    onPageChange(currentPage - 1)
                }
                className="
                    px-3
                    py-1
                    border
                    rounded
                "
            >
                Previous
            </button>

            <span>
                Page {currentPage} of {totalPages}
            </span>

            <button
                disabled={
                    currentPage === totalPages
                }
                onClick={() =>
                    onPageChange(currentPage + 1)
                }
                className="
                    px-3
                    py-1
                    border
                    rounded
                "
            >
                Next
            </button>

        </div>
    );
};

export default Pagination;