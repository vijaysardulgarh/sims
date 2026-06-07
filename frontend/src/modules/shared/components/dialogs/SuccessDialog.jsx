import Button from "../ui/Button";
import { CheckCircle } from "lucide-react";

const SuccessDialog = ({
    open,
    title = "Success",
    message = "Operation completed successfully",
    onClose,
}) => {

    if (!open) return null;

    return (
        <>
            <div
                className="
                    fixed
                    inset-0
                    bg-black/40
                    z-40
                "
            />

            <div
                className="
                    fixed
                    inset-0
                    flex
                    items-center
                    justify-center
                    z-50
                "
            >
                <div
                    className="
                        bg-white
                        rounded-xl
                        shadow-xl
                        p-6
                        w-full
                        max-w-md
                    "
                >
                    <div className="flex justify-center mb-4">
                        <CheckCircle
                            size={50}
                            className="text-green-600"
                        />
                    </div>

                    <h2
                        className="
                            text-xl
                            font-semibold
                            text-center
                        "
                    >
                        {title}
                    </h2>

                    <p
                        className="
                            text-center
                            text-gray-500
                            mt-2
                        "
                    >
                        {message}
                    </p>

                    <div className="mt-6 text-center">
                        <Button
                            onClick={onClose}
                        >
                            OK
                        </Button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default SuccessDialog;