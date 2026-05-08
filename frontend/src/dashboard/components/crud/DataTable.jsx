const DataTable = ({
  columns = [],
  data = [],
}) => {

  return (

    <div className="overflow-x-auto bg-white rounded-2xl shadow">

      <table className="min-w-full">

        <thead className="bg-gray-100">

          <tr>

            {columns.map((column) => (

              <th
                key={column.key}
                className="px-6 py-4 text-left text-sm font-semibold text-gray-700"
              >
                {column.label}
              </th>

            ))}

          </tr>

        </thead>

        <tbody>

          {data.map((row, index) => (

            <tr
              key={index}
              className="border-b"
            >

              {columns.map((column) => (

                <td
                  key={column.key}
                  className="px-6 py-4 text-sm text-gray-600"
                >
                  {row[column.key]}
                </td>

              ))}

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

};

export default DataTable;