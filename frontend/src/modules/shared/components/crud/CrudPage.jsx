import PageHeader from "../ui/PageHeader";

import SearchBar from "./SearchBar";
import BulkActions from "./BulkActions";
import DataTable from "./DataTable";
import Pagination from "./Pagination";

const CrudPage = ({

    title,
    subtitle,
    breadcrumbs,

    search,
    onSearch,

    columns,
    data,

    loading = false,

    currentPage,
    totalPages,
    onPageChange,

    selectedCount = 0,
    onBulkDelete,

    onView,
    onEdit,
    onDelete,

    headerActions,

}) => {

    return (

        <div className="space-y-6">

            <PageHeader

                title={title}

                subtitle={subtitle}

                breadcrumbs={
                    breadcrumbs
                }

                actions={
                    headerActions
                }

            />

            <div
                className="
                    bg-white
                    border
                    rounded-xl
                    shadow-sm
                    p-5
                    space-y-5
                "
            >

                <SearchBar
                    value={search}
                    onChange={onSearch}
                />

                <BulkActions
                    selectedCount={
                        selectedCount
                    }
                    onDelete={
                        onBulkDelete
                    }
                />

                <DataTable
                    loading={loading}
                    columns={columns}
                    data={data}
                    onView={onView}
                    onEdit={onEdit}
                    onDelete={onDelete}
                />

                <Pagination
                    currentPage={
                        currentPage
                    }
                    totalPages={
                        totalPages
                    }
                    onPageChange={
                        onPageChange
                    }
                />

            </div>

        </div>

    );

};

export default CrudPage;