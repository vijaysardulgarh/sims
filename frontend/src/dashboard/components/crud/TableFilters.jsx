const TableFilters = ({
    classFilter,
    setClassFilter,
    statusFilter,
    setStatusFilter,
  }) => {
  
    return (
  
      <div className="flex flex-col md:flex-row gap-4">
  
        {/* CLASS FILTER */}
        <select
          value={classFilter}
          onChange={(e) =>
            setClassFilter(e.target.value)
          }
          className="border border-gray-300 rounded-xl px-4 py-3"
        >
  
          <option value="">
            All Classes
          </option>
  
          <option value="9">
            Class 9
          </option>
  
          <option value="10">
            Class 10
          </option>
  
        </select>
  
        {/* STATUS FILTER */}
        <select
          value={statusFilter}
          onChange={(e) =>
            setStatusFilter(e.target.value)
          }
          className="border border-gray-300 rounded-xl px-4 py-3"
        >
  
          <option value="">
            All Status
          </option>
  
          <option value="Active">
            Active
          </option>
  
          <option value="Inactive">
            Inactive
          </option>
  
        </select>
  
      </div>
  
    );
  
  };
  
  export default TableFilters;