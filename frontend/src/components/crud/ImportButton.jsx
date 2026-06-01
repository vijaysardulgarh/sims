import Button from "../ui/Button";

const ImportButton = ({
    onImport,
}) => {

    return (

        <Button
            variant="primary"
            onClick={onImport}
        >
            Import
        </Button>

    );

};

export default ImportButton;