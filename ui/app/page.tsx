"use client";

import { useState, useEffect } from "react";
import { Separator } from "@/components/ui/separator";
import { ChatCard } from "@/components/chat";
import Link from "next/link";

function generateSessionId() {
  return Date.now().toString();
}

export default function Page() {
  const [sessionId, setSessionId] = useState<string | null>(null);

  useEffect(() => {
    if (!sessionId) {
      // Generate a new session ID (you can use any method to generate an ID)
      const newSessionId = generateSessionId(); // Replace this with your own logic
      setSessionId(newSessionId);
    }
  }, [sessionId]);

  return (
    <div className="mt-20 flex justify-center items-stretch">
      <div className="max-w-screen-lg w-full bg-background">
        <div className="p-4 md:p-8 flex flex-col">
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              {" "}
              {/* Right-align heading and tooltip */}
              <h2 className="text-5xl font-semibold tracking-tight">
                ASU AI 🔱
              </h2>
            </div>
          </div>
          <h3 className="text-sm pt-2 text-muted-foreground">
            Built with ❤️{" "}
            <Link
              className="text-gray-900 underline underline-offset-2"
              href="https://twitter.com/geeky_dan"
              target="_blank"
            >
              Dhanush Vardhan
            </Link>{" "}
            using
            <Link
              className="text-gray-900 underline underline-offset-2"
              href="github.com/dhanush17-tech/asu-ai"
              target="_blank"
            >
              using Embedchain
            </Link>{" "}
          </h3>
          <Separator className="my-4" />
          <div className="flex-1 overflow-y-auto max-h-fit">
            {/* <div className="bg-black/75 rounded-lg w-full p-8  h-[250px] justify-start flex flex-col">
              <h1 className="text-5xl text-white">We're offline!</h1>

              <h1 className="text-sm text-white/40 pt-2 pl-2">hold on for a little longer...</h1>
            </div> */}
            {sessionId !== null && <ChatCard sessionId={sessionId} />}
          </div>
        </div>
      </div>
    </div>
  );
}
