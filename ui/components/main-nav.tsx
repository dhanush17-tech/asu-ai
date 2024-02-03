"use client";

// import GitHubButton from "react-github-btn";

import Image from "next/image";
import Link from "next/link";

import { cn } from "@/lib/utils";
export function MainNav({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) {
  return (
    <nav
      className={cn(
        "flex flex-row justify-between items-center space-x-4 lg:space-x-6 w-full",
        className
      )}
      {...props}
    >
      <div className="flex items-center space-x-4 lg:space-x-6">
        <Link href="/">
          <Image
            src="https://i.pinimg.com/originals/65/e3/37/65e33744f64c4d1f8f082785761b205a.png"
            alt="Logo"
            width={50}
            height={50}
          />
        </Link>
      </div>

      <div className={cn("space-x-10", className)}>
        <Link
          href="https://twitter.com/geeky_dan"
          className="text-sm font-light text-muted-foreground transition-colors hover:text-primary hover:text-black"
        >
          Developer
        </Link>
        <Link
          href="github.com/dhanush17-tech/asu-ai"
          className="text-sm font-light text-muted-foreground transition-colors hover:text-primary hover:text-black"
          target="_blank"
        >
          GitHub
        </Link>
        {/* ... other links ... */}
      </div>
    </nav>
  );
}
