import { CheckCircle } from "lucide-react";

const Toast = ({
    message,
}) => {
    return (
        <div
            className="
                fixed
                top-5
                right-5
                bg-green-600
                text-white
                px-4
                py-3
                rounded-lg
                shadow-lg
                flex
                items-center
                gap-2
                z-[9999]
            "
        >
            <CheckCircle size={18} />

            {message}
        </div>
    );
};

export default Toast;