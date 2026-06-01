import { Upload, FileText } from "lucide-react";

const FileUpload = ({
    label,
    onChange,
    accept = "*",
    fileName = "",
}) => {
    return (
        <div className="space-y-2">

            {label && (
                <label className="block text-sm font-medium">
                    {label}
                </label>
            )}

            <label
                className="
                    border-2
                    border-dashed
                    rounded-lg
                    p-6
                    flex
                    flex-col
                    items-center
                    justify-center
                    cursor-pointer
                    hover:bg-gray-50
                "
            >
                <Upload size={28} />

                <span className="mt-2 text-sm">
                    Click to upload file
                </span>

                <input
                    type="file"
                    accept={accept}
                    onChange={(e) =>
                        onChange(
                            e.target.files[0]
                        )
                    }
                    className="hidden"
                />
            </label>

            {fileName && (
                <div
                    className="
                        flex
                        items-center
                        gap-2
                        text-sm
                        text-gray-600
                    "
                >
                    <FileText size={16} />
                    {fileName}
                </div>
            )}

        </div>
    );
};

export default FileUpload;