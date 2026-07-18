import { Link } from "react-router-dom";

const CrudHeader = ({
    title,
    description,
    addLabel = "Add",
    addPath,
    onAdd,
    children,
}) => {

    return (

        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">

            <div>

                <h1 className="text-3xl font-bold text-gray-800">
                    {title}
                </h1>

                {description && (
                    <p className="text-gray-500 mt-1">
                        {description}
                    </p>
                )}

            </div>

            <div className="flex gap-3">

                {addPath && (
                    <Link
                        to={addPath}
                        className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl font-medium transition"
                    >
                        {addLabel}
                    </Link>
                )}

                {!addPath && onAdd && (
                    <button
                        onClick={onAdd}
                        className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl font-medium transition"
                    >
                        {addLabel}
                    </button>
                )}

                {children}

            </div>

        </div>

    );

};

export default CrudHeader;