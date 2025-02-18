import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-2xl font-bold mb-4 text-purple-700">Welcome to the Player Stats App</h1>
      <Link
        href="/player_stats"
        className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-yellow-600 text-white hover:bg-yellow-500 text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
      >
        View Player Stats
      </Link>
    </div>
  );
}
