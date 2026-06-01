import Button from "../ui/Button";

const ExportButton = ({
    onExport,
}) => {

    return (

        <Button
            variant="secondary"
            onClick={onExport}
        >
            Export
        </Button>

    );

};

export default ExportButton;