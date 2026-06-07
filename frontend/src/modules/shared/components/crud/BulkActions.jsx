import Button
from "../ui/Button";

const BulkActions = ({
    selectedCount,
    onDelete,
}) => {

    if (selectedCount === 0)
        return null;

    return (

        <div
            className="
                bg-blue-50
                border
                rounded-md
                p-3
                flex
                justify-between
                items-center
            "
        >

            <span>
                {selectedCount}
                selected
            </span>

            <Button
                variant="danger"
                onClick={onDelete}
            >
                Bulk Delete
            </Button>

        </div>

    );
};

export default BulkActions;