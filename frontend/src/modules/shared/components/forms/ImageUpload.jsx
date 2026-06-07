import { Upload } from "lucide-react";

const ImageUpload = ({
    label,
    image,
    onChange,
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

                {image ? (

                    <img
                        src={image}
                        alt="Preview"
                        className="
                            h-32
                            w-32
                            object-cover
                            rounded-full
                        "
                    />

                ) : (

                    <>
                        <Upload size={28} />

                        <span className="mt-2 text-sm">
                            Upload Image
                        </span>
                    </>

                )}

                <input
                    type="file"
                    accept="image/*"
                    className="hidden"
                    onChange={(e) =>
                        onChange(
                            e.target.files[0]
                        )
                    }
                />

            </label>

        </div>
    );
};

export default ImageUpload;